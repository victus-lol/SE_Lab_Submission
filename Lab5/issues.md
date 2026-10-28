# Issues found and fixes made

**Student:** Aaryan Dubey  
**SRN:** PES2UG24CS016  

The line numbers below refer to the original `recruitment_tracker.py` file. The before and after reports are saved under `reports/before/` and `reports/after/`.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| SQL injection through applicant values | Security - Medium (Bandit B608) | 8 | Applicant details were inserted into SQL by building a string, so quotes or crafted input could change the query. | Replaced the interpolated SQL with placeholders and passed the values separately. |
| Executing the salary rule with `eval` | Security - Medium (Bandit B307) | 14 | The salary limit was evaluated as Python code, even though the example only needs a number. | Changed `shortlist` to accept a numeric salary limit and updated the example call. |
| Swallowed database errors | Reliability - Low (Bandit B110, Pylint W0718) | 26-29 | A broad exception handler ignored every error, making failed status updates look successful. | Removed the empty handler so database errors are visible to the caller. |
| Shortlist could return `None` | Correctness (Pylint R1710) | 12-20 | The function returned a list only when it was non-empty, so a role with no matching candidates had a different return type. | Return the list in all cases, including an empty list. |
| Unused variable | Maintainability (Pylint W0612, Flake8 F841) | 15 | `total_seen` was calculated but never used. | Removed the unused assignment. |
| Report file handling and CSV formatting | Reliability and portability (Pylint W1514/R1732) | 31-35 | The file was opened without an encoding or a context manager, and joining fields with commas did not safely escape CSV values. | Used `csv.writer` inside a `with` block and specified UTF-8 encoding. |

The final checks reported a Pylint score of 10.00/10, no Bandit findings, and no Flake8 output.
