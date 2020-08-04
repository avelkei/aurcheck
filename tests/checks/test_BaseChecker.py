def test_empty_dir(init_checker):
	from checks.BaseChecker import BaseChecker
	checker = init_checker(BaseChecker, "test_data/empty_dir")
	checker.check()
	assert checker.fail_message == "no files to check"

def test_all_empty_files(init_checker):
	from checks.BaseChecker import BaseChecker
	checker = init_checker(BaseChecker, "test_data/all_empty_files")
	checker.check()
	assert checker.fail_message == "no files to check"
