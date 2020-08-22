try:
	import importlib.resources as pkg_resources
except ImportError:
	import importlib_resources as pkg_resources

from .BaseChecker import BaseChecker
from .util.CheckResult import CheckResult
from .util.Severity import Severity
from aurcheck import yara_rules

class YaraChecker(BaseChecker):
	def check_fn(self):
		from shutil import which
		import subprocess

		if which("yara") is None:
			self.fail_message = "YARA can't be found"
			return

		if which("yextend") is None:
			self.fail_message = "yextend can't be found"
			return

		import json
		import os.path

		def get_offset_lines(filepath, offsets):
			match_lines = []
			file_offset = 0
			with open(filepath, "r") as f:
				try:
					for (i, line) in enumerate(f):
						if len(offsets) == 0:
							break

						line_length = len(line)

						if file_offset + line_length <= offsets[0]:
							file_offset += line_length
							continue

						match_lines.append((i+1, line.rstrip()))
						offsets = list(filter(lambda offset: offset > file_offset + line_length, offsets))
						file_offset += line_length
				except UnicodeDecodeError:
					return None

			return match_lines

		# yextend doesn't scan subdirectories so we'll run it file by file
		def scan_file(filepath: str, rule_file: str, match_severity: Severity):
			abs_path = os.path.abspath(filepath)
			yextend_process = subprocess.run(["run_yextend", "-r", rule_file, "-t", abs_path, "-j"], capture_output=True)
			try:
				yextend_output = json.loads(yextend_process.stdout.decode("utf-8"))[0]
			except json.decoder.JSONDecodeError:
				self.add_result_item(CheckResult(severity=Severity.INFO, filepath=filepath, message=f"did not get expected json output, yextend output: {yextend_process.stdout.decode('utf-8')}"))
				return

			if "yara_matches_found" in yextend_output and yextend_output["yara_matches_found"] is True:
				scan_results = yextend_output["scan_results"]
				for sr in scan_results:
					rule_id = sr["yara_rule_id"]
					match_offsets = list(map(lambda ofs: int(ofs.split(":")[0], 16), sr["detected offsets"]))
					match_lines = get_offset_lines(filepath, match_offsets) # tuple(line_index, line_text)
					if match_lines is None:
						self.add_result_item(CheckResult(severity=match_severity, filepath=filepath, match_name=rule_id, message="failed to read file, probably a binary file"))
						return

					for (line_num, line_text) in match_lines:
						self.add_result_item(CheckResult(severity=match_severity, filepath=filepath, line_number=line_num, line_content=line_text, match_name=rule_id))
		
		with pkg_resources.path(yara_rules, "index_warn.yar") as path_warn:
			with pkg_resources.path(yara_rules, "index_block.yar") as path_block:
				for filepath in self.package_files:
					scan_file(filepath, str(path_warn), Severity.WARN)
					scan_file(filepath, str(path_block), Severity.BLOCK)
