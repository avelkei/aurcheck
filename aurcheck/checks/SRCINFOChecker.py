from .BaseChecker import BaseChecker
from .util.CheckResult import CheckResult
from .util.Severity import Severity

class SRCINFOChecker(BaseChecker):
	def check_fn(self):
		import os.path
		import re

		if not os.path.isfile(os.path.join(self.package_path, "PKGBUILD")) or not os.path.isfile(os.path.join(self.package_path, ".SRCINFO")):
			self.fail_message = "file missing, can't check .SRCINFO"
			return

		pkgbuild_contents = open(os.path.join(self.package_path, "PKGBUILD")).read()
		srcinfo_contents = open(os.path.join(self.package_path, ".SRCINFO")).read()

		# Check if there are any URLs in the PKGBUILD file that are not present in .SRCINFO
		# https://stackoverflow.com/a/3809435
		url_regex = re.compile(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)")

		pkgbuild_urls = url_regex.findall(pkgbuild_contents)
		srcinfo_urls = url_regex.findall(srcinfo_contents)

		for url in pkgbuild_urls:
			if url not in srcinfo_urls:
				self.add_result_item(CheckResult(severity=Severity.WARN, message=f"PKGBUILD contains a URL that isn't found in .SRCINFO: {url}"))
