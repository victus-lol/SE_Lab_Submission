"""Track applicants and shortlist candidates against a salary limit."""

import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute(
    "CREATE TABLE applicants ("
    "id INTEGER PRIMARY KEY, name TEXT, role TEXT, "
    "expected_salary INTEGER, status TEXT)"
)


def add_applicant(name, role, expected_salary, status="applied"):
    """Add one applicant to the in-memory tracker."""
    connection.execute(
        "INSERT INTO applicants (name, role, expected_salary, status) "
        "VALUES (?, ?, ?, ?)",
        (name, role, expected_salary, status),
    )
    connection.commit()


def shortlist(role, salary_limit):
    """Return applicants for a role who meet the salary limit."""
    rows = connection.execute(
        "SELECT name, expected_salary FROM applicants WHERE role = ?", (role,)
    ).fetchall()
    result = []
    for name, salary in rows:
        if salary <= salary_limit:
            result.append(name)
    return result


def update_status(applicant_id, status):
    """Update the hiring status for an applicant."""
    connection.execute(
        "UPDATE applicants SET status = ? WHERE id = ?", (status, applicant_id)
    )
    connection.commit()


def export_report(path):
    f = open(path, "w")
    for row in connection.execute("SELECT name, role, status FROM applicants"):
        f.write(",".join(row) + "\n")
    f.close()


def count_by_status(status):
    """Return the number of applicants with the given status."""
    return connection.execute(
        "SELECT COUNT(*) FROM applicants WHERE status = ?", (status,)
    ).fetchone()[0]


def main():
    """Run a short example of the recruitment tracker."""
    add_applicant("Nina", "analyst", 600000)
    add_applicant("Omar", "analyst", 750000, "interview")
    add_applicant("Priya", "developer", 900000)
    update_status(1, "interview")
    print(shortlist("analyst", 650000))
    export_report("applicants_report.csv")
    print(count_by_status("interview"), "in interview")


if __name__ == "__main__":
    main()
