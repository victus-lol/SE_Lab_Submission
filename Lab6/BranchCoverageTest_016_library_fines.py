"""Tests that exercise both outcomes of the module's decisions."""

import pytest

from library_fines import can_borrow, late_fine, renewal_status


@pytest.mark.parametrize(
    ("member", "days_kept", "damaged", "expected"),
    [
        ("student", 14, False, 0),
        ("student", 15, False, 2),
        ("faculty", 30, False, 0),
        ("faculty", 31, True, 151),
        ("guest", 55, False, 200),
        ("guest", 56, True, 350),
    ],
)
def test_late_fine_branches(member, days_kept, damaged, expected):
    assert late_fine(member, days_kept, damaged) == expected


@pytest.mark.parametrize(
    ("member", "books_held", "pending_fine", "expected"),
    [
        ("student", 2, 100, True),
        ("student", 3, 0, False),
        ("faculty", 9, 0, True),
        ("faculty", 10, 0, False),
        ("guest", 0, 101, False),
    ],
)
def test_borrowing_branches(member, books_held, pending_fine, expected):
    assert can_borrow(books_held, pending_fine, member) is expected


@pytest.mark.parametrize(
    ("times_renewed", "has_reservation", "days_left", "expected"),
    [
        (0, False, 1, "renewed"),
        (0, False, -1, "overdue"),
        (2, False, 1, "limit reached"),
        (0, True, 1, "denied"),
    ],
)
def test_renewal_branches(times_renewed, has_reservation, days_left, expected):
    assert renewal_status(times_renewed, has_reservation, days_left) == expected


@pytest.mark.parametrize(
    ("member", "days_kept", "message"),
    [("visitor", 1, "unknown member"), ("student", -1, "invalid days")],
)
def test_invalid_fine_inputs(member, days_kept, message):
    with pytest.raises(ValueError, match=message):
        late_fine(member, days_kept, False)
