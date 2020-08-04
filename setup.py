import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="aurcheck",
	version="0.1",
	author="Adam Velkei",
	author_email="adam@avelkei.eu",
	description="Scans an AUR package for potential threats",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/avelkei/aurcheck",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
	],
	python_requires='>=3.8',
)
