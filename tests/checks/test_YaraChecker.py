def test_empty_dir(init_checker):
	from checks.YaraChecker import YaraChecker
	checker = init_checker(YaraChecker, "test_data/edge_cases/empty_dir")
	checker.check()
	assert checker.fail_message is None and len(checker.results) == 0

def test_all_empty_files(init_checker):
	from checks.YaraChecker import YaraChecker
	checker = init_checker(YaraChecker, "test_data/edge_cases/all_empty_files")
	checker.check()
	assert checker.fail_message is None and len(checker.results) == 0
