from checks.BaseChecker import BaseChecker
from checks.util.CheckResult import CheckResult
from checks.util.Severity import Severity

class ClamAvChecker(BaseChecker):
	def check_fn(self):
		from shutil import which
		import subprocess

		if which("clamscan") is None:
			self.fail_message = "ClamAV (clamscan) can't be found"
			return

		clam_process = subprocess.run(["clamscan", "-r", self.package_path], capture_output=True)

		if clam_process.returncode == 0: # ClamAV says clean
			self.add_result_item(CheckResult(severity=Severity.INFO, message="ClamAV found no malicious files"))
		elif clam_process.returncode == 1: # ClamAV found malicious files
			clam_output = clam_process.stdout.decode("utf-8")
			self.add_result_item(CheckResult(severity=Severity.BLOCK, message=clam_output))
		elif clam_process.returncode == 2: # ClamAV failed to complete
			self.fail_message = "ClamAV failed with an error"
