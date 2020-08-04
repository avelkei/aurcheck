import pytest

@pytest.fixture
def list_files():
	def files_in_dir(path):
		import os
		import os.path

		files = []
		for root, dirs, files in os.walk(path):
			if ".git" in dirs:
				dirs.remove(".git")
			for name in files:
				file_path = os.path.join(root, name)
				if os.path.getsize(file_path) > 0:
					files.append(file_path)
		return files
	return files_in_dir

@pytest.fixture
def init_checker(list_files):
	def init(cls, path):
		checker = cls(path, list_files(path))
		return checker
	return init
