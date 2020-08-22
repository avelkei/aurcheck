from .BaseChecker import BaseChecker
from .util.CheckResult import CheckResult
from .util.Severity import Severity

class SRCINFOChecker(BaseChecker):
	def check_fn(self):
		import os.path
		import re

		if not os.path.isfile(os.path.join(self.package_path, "PKGBUILD")) \
			or not os.path.isfile(os.path.join(self.package_path, ".SRCINFO")):
			self.fail_message = "file missing, can't check .SRCINFO"
			return

		try:
			pkgbuild_contents = open(os.path.join(self.package_path, "PKGBUILD")).read()
		except UnicodeDecodeError:
			pkgbuild_contents = open(os.path.join(self.package_path, "PKGBUILD"), encoding="ISO-8859-1").read()
		
		try:
			srcinfo_contents = open(os.path.join(self.package_path, ".SRCINFO")).read()
		except UnicodeDecodeError:
			srcinfo_contents = open(os.path.join(self.package_path, ".SRCINFO"), encoding="ISO-8859-1").read()

		# Find variables in PKGBUILD
		pkgbuild_vars = {}
		bash_var_pattern = re.compile(r"([_a-zA-Z0-9]+)=([\"\'].+[\"\']|[^\s]+)")
		for line in pkgbuild_contents.splitlines():
			match = bash_var_pattern.match(line.strip())
			if match is not None:
				pkgbuild_vars[match.group(1)] = match.group(2)

		# Substitute variables with their values in PKGBUILD contents
		# (where they're not bash formatted expressions)
		for (var_name, var_value) in pkgbuild_vars.items():
			pkgbuild_contents = re.sub(rf"(\${var_name}|\$\{{{var_name}\}})", var_value.strip("'\""), pkgbuild_contents)
		
		# Check if there are any URLs in the PKGBUILD file that are not present in .SRCINFO
		url_regex = re.compile(r"(https?:\/\/[^\[\]\(\)\s'\"]+)")

		pkgbuild_urls = url_regex.findall(pkgbuild_contents)
		srcinfo_urls = url_regex.findall(srcinfo_contents)

		# Remove duplicates
		pkgbuild_urls = list(set(pkgbuild_urls))

		for url in pkgbuild_urls:
			if url not in srcinfo_urls:
				self.add_result_item(CheckResult(severity=Severity.WARN, 
					message=f"PKGBUILD contains URL which can't be found in .SRCINFO: {url}"))
