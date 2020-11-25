from .BaseChecker import BaseChecker
from .util.CheckResult import CheckResult
from .util.Severity import Severity

class ShellChecker(BaseChecker):
	def check_fn(self):
		from shutil import which
		import json
		import os.path
		import subprocess
		import sys

		if which("shellcheck") is None:
			self.fail_message = "shellcheck can't be found"
			return

		ignore_files = [
			".gitignore",
			".SRCINFO"
		]

		# Certain files tend to generate a high number of messages which can be safely ignored
		ignore_codes = {
			"*": [
				2034, # variable appears unused
				2148, # missing shebang directive
			],
			"PKGBUILD": [
				2154, # variable referenced but not assigned
			],
		}

		def get_shell_scripts(filepath_list):
			"""Select files which look like shell scripts using `bash -n <filepath>`"""
			sh_files = []

			for filepath in filepath_list:
				if os.path.basename(filepath) in ignore_files:
					continue
				
				bash_process = subprocess.run(["bash", "-n", filepath], capture_output=True)
				if bash_process.returncode == 0:
					sh_files.append(filepath)

			return sh_files

		def check_file(filepath):
			shellcheck_process = subprocess.run(["shellcheck", "--format=json1", "--severity=warning", filepath], capture_output=True)

			if shellcheck_process.returncode == 0: # Successful check, no issues
				self.add_result_item(CheckResult(severity=Severity.INFO, message="Shellcheck found no issues"))
			elif shellcheck_process.returncode == 1: # Successful check, some issues
				shellcheck_output = shellcheck_process.stdout.decode("utf-8")
				results = parse_output(shellcheck_output)

				for result in results:
					self.add_result_item(result)
			elif shellcheck_process.returncode == 2: # Error while checking
				self.fail_message = "shellcheck failed with an error"
			elif shellcheck_process.returncode in [3, 4]: # Bad arguments
				self.fail_message = "Wrong arguments passed to shellcheck"

		def parse_output(output):
			result_items = []

			parsed_output = json.loads(output)["comments"]
			for result in parsed_output:
				result_filename = result["file"]
				result_line = result["line"]
				result_level = result["level"]
				result_code = result["code"]
				result_message = result["message"]

				if result_code in ignore_codes["*"]:
					continue

				filename_stripped = os.path.basename(result_filename)
				if filename_stripped in ignore_codes:
					if result_code in ignore_codes[filename_stripped]:
						continue

				result_items.append(CheckResult(
					severity=Severity.WARN,
					filepath=result_filename,
					line_number=result_line,
					match_name=f"shellcheck {result_level} code: {result_code}",
					message=result_message
				))

			return result_items

		sh_files = get_shell_scripts(self.package_files)
		for filepath in sh_files:
			check_file(filepath)

		#print(self.package_files, file=sys.stderr)
		#print(sh_files, file=sys.stderr)
		#print(self.results, file=sys.stderr)
