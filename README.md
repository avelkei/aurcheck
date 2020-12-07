# aurcheck

Runs safety checks on AUR packages (ideally before building and installing)

## Usage

```
aurcheck [-h] [-d DISABLE] [--only ONLY] [-v] [-l [LOGFILE]] package_path

positional arguments:
  package_path          path to directory containing PKGBUILD and other build files

optional arguments:
  -h, --help                          show this help message and exit
  -d DISABLE, --disable DISABLE       disable certain checks
  --only ONLY                         run a single specified checker
  -v, --verbose                       print info messages as well
  -l [LOGFILE], --logfile [LOGFILE]   write output to a log file (default: aurcheck.log)
```

### Running aurcheck

Assuming we have an AUR package in a directory (by calling `git clone https://aur.archlinux.org/firefox-beta-bin.git` for example), we can do the following:

Default behaviour: run all checkers on the directory and its files, print results to the standard output\
`aurcheck firefox-beta-bin`

Run checks with ClamAVChecker disabled. Checker class names can be referenced case-insensitively and can be shortened to your liking as long as it specifies exactly one class.\
`aurcheck -d clamav firefox-beta-bin`

Multiple checkers disabled\
`aurcheck -d yara -d clamav firefox-beta-bin`

Run only ClamAVChecker\
`aurcheck --only clamav firefox-beta-bin`

Write output to a file (if no filename is specified after `-l`, the file will be placed in the current working directory with the name `aurcheck.log`)\
`aurcheck -l test_output.txt firefox-beta-bin`

In order to get the most out of aurcheck, it should be run after all source files defined in the PKGBUILD file have been downloaded, but before the build process actually starts. 

## Operation

aurcheck comes with a number of checker classes, each of which performs a specific check on package files.

### Severity

Every check finding has a severity level:
- `INFO`: informational, debug messages, not printed by default (use `-v` or `--verbose` to show these)
- `WARN`: possibly harmful findings which should be presented to the user for review
- `BLOCK`: known harmful findings which should be always blocked

Severity is represented with an enum, which can be found in checks/util/Severity.py

The severity of the findings determines aurcheck's exit code:
- 0 - No issues found
- 1 - Exited with an error
- 2 - WARN level issues found
- 3 - BLOCK level issues found

### Check results

Checker classes generate a list of CheckResult objects for every issue they find.\
CheckResult is represented with a dataclass in checks/util/CheckResult.py with the following fields:
- `severity`: Severity
- `checker`: str = None
- `filepath`: str = None
- `line_number`: int = None
- `line_content`: str = None
- `match_name`: str = None
- `message`: str = None

### Checker classes

All checker class instances are created with the following variables set:\
`self.package_path` - the directory path passed to aurcheck\
`self.package_files` - list of files in `package_path` (excluding files in the `.git` subdirectory by default)

## How to create a checker class

```python
# from checks/ClamAvChecker.py

# Create a Python class in the checks directory
# Make the following changes in the aurcheck.py file:
#   - import the new checker class
#   - add the checker class to the list of available checkers

# Import these objects and classes below
from checks.BaseChecker import BaseChecker
from checks.util.CheckResult import CheckResult
from checks.util.Severity import Severity

# Make sure that the checker class inherits from BaseChecker
class ClamAvChecker(BaseChecker):
  # Override the check_fn method with you own logic
  def check_fn(self):
    from shutil import which
    import subprocess

    # If your checker can't run for any reason, you can put an error message
    # in self.fail_message. If self.fail_message is set to anything other than
    # its default None value, the checker's results will be discarded.
    if which("clamscan") is None:
      self.fail_message = "ClamAV (clamscan) can't be found"
      return

      clam_process = subprocess.run(["clamscan", "-r", self.package_path], capture_output=True)

    # New CheckResult objects can be created like this:
    # CheckResult(severity=Severity.INFO, message="ClamAV found no malicious files")
    #
    # Use the self.add_result_item method to add the CheckResult objects to the
    # checkers final results.
    if clam_process.returncode == 0: # ClamAV says clean
      self.add_result_item(CheckResult(severity=Severity.INFO, message="ClamAV found no malicious files"))
    elif clam_process.returncode == 1: # ClamAV found malicious files
      clam_output = clam_process.stdout.decode("utf-8")
      self.add_result_item(CheckResult(severity=Severity.BLOCK, message=clam_output))
    elif clam_process.returncode == 2: # ClamAV failed to complete
      self.fail_message = "ClamAV failed with an error"
```

## Testing

Make sure you have `pytest` installed and execute `run_tests.sh` from the project's root directory.\
Checker tests can be added in the tests/checks directory.
