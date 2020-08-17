from dataclasses import dataclass
from .Severity import Severity

@dataclass
class CheckResult:
	severity: Severity
	checker: str = None
	filepath: str = None
	line_number: int = None
	line_content: str = None
	match_name: str = None
	message: str = None
