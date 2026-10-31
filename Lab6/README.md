# L6_L7_14_library_fines — Library Fines

Lab 6: Code and Branch Coverage

## About

A small Python module that works out late return fines by member type, checks whether a member can borrow more books and decides if a book can be renewed.

## Files

| File | Description |
|------|-------------|
| `library_fines.py` | The module under test |
| `test_library_fines.py` | Starter test file |
| `CodeCoverageTest_016_library_fines.py` | Test cases used for line coverage |
| `BranchCoverageTest_016_library_fines.py` | Test cases used for branch coverage |
| `code_coverage_output.txt` and `code_coverage_report.txt` | Captured output from the line coverage run |
| `branch_coverage_output.txt` and `branch_coverage_report.txt` | Captured output from the branch coverage run |

Refer to the lab handout for instructions.

## Coverage results

The fine tests use the rates and limits defined in `library_fines.py`. The line coverage run passed all 5 tests and measured 100% coverage (32 of 32 statements). The branch coverage run passed all 17 cases and measured 100% coverage, including all 22 branch paths.

Run from this folder with:

```bash
python -m coverage run -m pytest CodeCoverageTest_016_library_fines.py
python -m coverage report -m library_fines.py
python -m coverage erase
python -m coverage run --branch -m pytest BranchCoverageTest_016_library_fines.py
python -m coverage report -m library_fines.py
```
