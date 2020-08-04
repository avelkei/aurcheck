import aurcheck
import pytest

@pytest.fixture
def init_aurcheck():
	def init(args):
		default_args = {
			"path": "",
			"verbose": False,
			"logfile": None,
			"only": None,
			"disable": None
		}
		args = {**default_args, **args}
		return aurcheck.Aurcheck(args)
	return init

def test_init_without_valid_dir(capsys, init_aurcheck):
	# Failing with error code -1 if the given path is not an existing directory
	with pytest.raises(SystemExit) as excinfo:
		ac = init_aurcheck({"path": "non_existent_directory"})
		assert excinfo.value.code == -1

def test_get_checker_from_name(init_aurcheck):
	class TestChecker1:
		pass

	class TestChecker2:
		pass

	class AnotherTestChecker:
		pass

	ac = init_aurcheck({"path": "tests/test_data/aur_package_clean"})
	ac.available_checks = [TestChecker1, TestChecker2, AnotherTestChecker]

	# Simple lookups
	assert ac.get_checker_from_name("testchecker1") == TestChecker1
	assert ac.get_checker_from_name("another") == AnotherTestChecker

	# Ambiguous name given
	with pytest.raises(KeyError, match="Error: ambiguous checker name.*"):
		ac.get_checker_from_name("test")

	# No matches
	with pytest.raises(KeyError, match="Error: can't find checker matching.*"):
		ac.get_checker_from_name("fake_test_checker")

def test_select_checks(init_aurcheck):
	class TestChecker1:
		pass

	class TestChecker2:
		pass

	class AnotherTestChecker:
		pass

	# Default behaviour - no exceptions specified, every checker is enabled to run
	ac = init_aurcheck({"path": "tests/test_data/aur_package_clean"})
	ac.available_checks = [TestChecker1, TestChecker2, AnotherTestChecker]

	ac.select_checks()
	assert ac.enabled_checks == ac.available_checks

	# Single checker enabled
	ac = init_aurcheck({"path": "tests/test_data/aur_package_clean", "only": "testchecker1"})
	ac.available_checks = [TestChecker1, TestChecker2, AnotherTestChecker]

	ac.select_checks()
	assert ac.enabled_checks == [TestChecker1]

	# Single checker disabled
	ac = init_aurcheck({"path": "tests/test_data/aur_package_clean", "disable": ["testchecker2"]})
	ac.available_checks = [TestChecker1, TestChecker2, AnotherTestChecker]

	ac.select_checks()
	assert ac.enabled_checks == [TestChecker1, AnotherTestChecker]

	# Multiple checkers disabled
	ac = init_aurcheck({"path": "tests/test_data/aur_package_clean", "disable": ["testchecker2", "another"]})
	ac.available_checks = [TestChecker1, TestChecker2, AnotherTestChecker]

	ac.select_checks()
	assert ac.enabled_checks == [TestChecker1]

	# All checkers disabled
	ac = init_aurcheck({"path": "tests/test_data/aur_package_clean", "disable": ["testchecker1", "testchecker2", "another"]})
	ac.available_checks = [TestChecker1, TestChecker2, AnotherTestChecker]

	with pytest.raises(KeyError, match="There are no enabled checks to run"):
		ac.select_checks()
