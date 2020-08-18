#!/usr/bin/env python

import argparse
import os.path
import re
import sys

from aurcheck.checks.GitChecker import GitChecker
from aurcheck.checks.YaraChecker import YaraChecker
from aurcheck.checks.ClamAvChecker import ClamAvChecker
from aurcheck.checks.SRCINFOChecker import SRCINFOChecker
from aurcheck.checks.util.Severity import Severity

class Aurcheck:
	available_checks = [
		#GitChecker,
		YaraChecker,
		ClamAvChecker,
		SRCINFOChecker
	]
	
	def __init__(self, args: dict):
		if not os.path.isdir(args["path"]):
			print("Invalid path, the program must be called with a directory parameter")
			sys.exit(1)

		self.available_checks = Aurcheck.available_checks
		self.package_path = args["path"]
		self.is_git_repo = os.path.isdir(f"{self.package_path}/.git")
		self.verbose_output = args["verbose"]
		self.logfile = args["logfile"]
		self.results = []
		self.exit_code = 0
		self.disabled_checks = None
		self.single_check = args["only"]

		if args["disable"] is not None:
			self.disabled_checks = list(map(lambda s: s.lower(), args["disable"]))

	def get_checker_from_name(self, name):
		matches = [checker for checker in self.available_checks if checker.__name__.lower().startswith(name.lower())]
		if len(matches) == 0:
			raise KeyError(f"Error: can't find checker matching '{name}'\nAvailable checkers: {', '.join([ch.__name__ for ch in self.available_checks])}")
		if len(matches) > 1:
			raise KeyError(f"Error: ambiguous checker name '{name}', try again with more characters\nAvailable checkers: {', '.join([ch.__name__ for ch in self.available_checks])}")

		return matches[0]

	def select_checks(self):
		self.enabled_checks = self.available_checks

		try:
			if self.single_check is not None:
				self.enabled_checks = [self.get_checker_from_name(self.single_check)]
			elif self.disabled_checks is not None:
				disabled_check_classes = list(map(self.get_checker_from_name, self.disabled_checks))
				self.enabled_checks = [ch for ch in self.enabled_checks if ch not in disabled_check_classes]
		except KeyError as e:
			raise e

		if len(self.enabled_checks) == 0:
			raise KeyError("There are no enabled checks to run")

	def find_files(self):
		# Files in package folder excluding the .git directory
		self.package_files = []
		for root, dirs, files in os.walk(self.package_path):
			if ".git" in dirs:
				dirs.remove(".git")
			for name in files:
				file_path = os.path.join(root, name)
				if os.path.getsize(file_path) > 0:
					self.package_files.append(file_path)

	def prepare(self):
		try:
			self.select_checks()
		except KeyError as err:
			print(err)
			sys.exit(1)

		self.find_files()

	def run_checks(self):
		for checker_class in self.enabled_checks:
			checker = checker_class(self.package_path, self.package_files)
			check_result = checker.check()

			if check_result["fail_message"] is not None:
				pass
			elif check_result["fail_message"] is None and len(check_result["results"]) == 0:
				pass
			else:
				self.results.extend(check_result["results"])

	def write_results(self):
		result_items_by_severity = {
			"INFO": [result for result in self.results if result.severity == Severity.INFO],
			"WARN": [result for result in self.results if result.severity == Severity.WARN],
			"BLOCK": [result for result in self.results if result.severity == Severity.BLOCK],
		}

		if len(result_items_by_severity["BLOCK"]) > 0:
			self.exit_code = 3
		elif len(result_items_by_severity["WARN"]) > 0:
			self.exit_code = 2

		result_items_by_file = {}
		results_without_filepath = []

		for item in self.results:
			if not self.verbose_output and item.severity == Severity.INFO:
				continue
			 
			if item.filepath is None or len(str(item.filepath)) == 0:
				results_without_filepath.append(item)
			else:
				if item.filepath not in result_items_by_file:
					result_items_by_file[item.filepath] = []

				result_items_by_file[item.filepath].append(item)

		result_strings = []

		for (filepath, items) in result_items_by_file.items():
			if len(items) > 0:
				result_strings.append(filepath)
				file_items_by_match = {}

				for item in items:
					if item.match_name is not None and len(item.match_name) > 0:
						if item.match_name not in file_items_by_match:
							file_items_by_match[item.match_name] = []
						file_items_by_match[item.match_name].append(item)
				for (match, match_items) in file_items_by_match.items():
					result_strings.append(f"  {match_items[0].severity.name} -- {match}")
					for item in match_items:
						line = f"    {str(item.line_number).ljust(5)} {item.line_content}"
						if item.message is not None:
							line += f" ({item.message})"
						result_strings.append(line)

				result_strings.append("")
		
		for item in results_without_filepath:
			result_strings.append(f"  {item.severity.name} -- {item.checker} -- {item.message}")

		result = "\n".join(result_strings)

		if self.logfile is None:
			if len(result) > 0:
				print(result)
		else:
			if len(result) > 0:
				with open(self.logfile, "a") as f:
					f.write(result + "\n")

	def main(args):
		import textwrap

		checker_names = [checker.__name__ for checker in Aurcheck.available_checks]

		parser = argparse.ArgumentParser(
			prog="aurcheck",
			description="Scans an AUR package for potential threats",
			epilog="Available checkers:\n" + textwrap.indent("\n".join(checker_names), "  "),
			formatter_class=argparse.RawDescriptionHelpFormatter)
		parser.add_argument("path", metavar="package_path", type=str, help="path to directory containing PKGBUILD and other build files")
		parser.add_argument("-d", "--disable", action="append", help="disable certain checks")
		parser.add_argument("--only", help="run a single specified checker")
		parser.add_argument("-v", "--verbose", action="store_true", help="print info messages")
		parser.add_argument("-l", "--logfile", nargs="?", const="aurcheck.log", help="write output to a log file (default: aurcheck.log)")

		parsed_args = parser.parse_args(args=args[1:])
		parsed_args = vars(parsed_args)

		ac = Aurcheck(parsed_args)
		ac.prepare()
		ac.run_checks()
		ac.write_results()

		# Exit codes:
		# 0 - no issues found
		# 1 - exited due to an error
		# 2 - warning level issues found, might need user confirmation
		# 3 - known harmful matches found, should abort unless user gives explicit permission
		sys.exit(ac.exit_code)

if __name__ == "__main__":
	Aurcheck.main(sys.argv)