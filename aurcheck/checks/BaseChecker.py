from typing import List

from checks.util.CheckResult import CheckResult
from checks.util.Severity import Severity

class BaseChecker:
	"""Base class for package checker classes

	All checker classes must inherit from this class.
	"""
	def __init__(self, path: str, files: List[str]):
		self.package_path = path
		self.package_files = files
		self.results = []
		self.fail_message = None

	def check_fn(self):
		if len(self.package_files) == 0:
			self.fail_message = "no files to check"

	def check(self):
		self.check_fn()
		if self.fail_message is not None and len(self.fail_message) == 0:
			self.fail_message = "this checker did not provide a failure message"
		return {
			"results": self.results,
			"fail_message": self.fail_message
		}

	def add_result_item(self, item: CheckResult):
		item.checker = self.__class__.__name__
		self.results.append(item)
