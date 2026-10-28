# Reflection

**Student:** Aaryan Dubey  
**SRN:** PES2UG24CS016  

The handout asks for four reflection answers, but it does not include a list of questions. I wrote the four questions below from the lab's learning outcomes and answered them based on this exercise.

### 1. What does static analysis help you find before running a program?

It points out risks and code problems by inspecting the source. In this tracker, the reports helped catch unsafe SQL construction, use of `eval`, an exception that hid errors, and several readability issues.

### 2. How did Pylint, Bandit, and Flake8 differ in this exercise?

Bandit focused on risky patterns, such as `eval` and SQL built from input. Pylint gave broader feedback about correctness and maintainability, including the missing return and unused variable. Flake8 highlighted formatting problems like long lines and trailing whitespace.

### 3. Which changes mattered most, and why?

The SQL placeholders and removal of `eval` mattered most because they reduced the chance that input could alter a query or run as code. Returning an empty list consistently and allowing database errors to surface also made the program's behavior easier to understand.

### 4. Can static analysis prove that a program is correct?

No. It can flag known patterns, but it cannot confirm every behavior or replace running the program with realistic inputs. Here, I also ran the example and checked that it still shortlisted the candidate, counted interview applicants, and wrote the CSV report.
