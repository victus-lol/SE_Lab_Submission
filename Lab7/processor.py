"""Library fines, borrowing, and renewal rules with strict input validation."""

DAILY_FINE = {"student": 2, "faculty": 1, "guest": 5}

def _require_member(member):
    if not isinstance(member, str) or member not in DAILY_FINE:
        raise ValueError("unknown member")

def _require_int(value, message, *, minimum=None):
    if type(value) is not int or (minimum is not None and value < minimum):
        raise ValueError(message)

def late_fine(member, days_kept, is_damaged):
    _require_member(member)
    _require_int(days_kept, "invalid days", minimum=0)
    if type(is_damaged) is not bool:
        raise ValueError("invalid damage flag")
    loan_days = 30 if member == "faculty" else 14
    overdue = days_kept - loan_days
    fine = min(overdue * DAILY_FINE[member], 200) if overdue > 0 else 0
    return fine + (150 if is_damaged else 0)

def can_borrow(books_held, pending_fine, member):
    _require_int(books_held, "invalid books held", minimum=0)
    _require_int(pending_fine, "invalid pending fine", minimum=0)
    _require_member(member)
    if pending_fine > 100:
        return False
    return books_held < (10 if member == "faculty" else 3)

def renewal_status(times_renewed, has_reservation, days_left):
    _require_int(times_renewed, "invalid renewal count", minimum=0)
    if type(has_reservation) is not bool:
        raise ValueError("invalid reservation flag")
    _require_int(days_left, "invalid days left")
    if has_reservation:
        return "denied"
    if times_renewed >= 2:
        return "limit reached"
    if days_left < 0:
        return "overdue"
    return "renewed"

if __name__ == "__main__":
    print("Student fine (15 days):", late_fine("student", 15, False))
    print("Faculty borrowing (9 books, no fine):", can_borrow(9, 0, "faculty"))
    print("Renewal (no reservation, 2 days left):", renewal_status(0, False, 2))
