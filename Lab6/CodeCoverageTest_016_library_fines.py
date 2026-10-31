"""Tests aimed at executing every line in the library fines module."""

import pytest

from library_fines import can_borrow, late_fine, renewal_status


def test_late_fine_examples():
    assert late_fine("student", 10, False) == 0
    assert late_fine("student", 15, False) == 2
    assert late_fine("faculty", 31, True) == 151


def test_late_fine_rejects_unknown_member_and_negative_days():
    with pytest.raises(ValueError, match="unknown member"):
        late_fine("visitor", 1, False)
    with pytest.raises(ValueError, match="invalid days"):
        late_fine("student", -1, False)


def test_late_fine_cap_and_damage_addition():
    assert late_fine("guest", 100, False) == 200
    assert late_fine("guest", 100, True) == 350


def test_borrowing_decisions():
    assert can_borrow(2, 0, "student") is True
    assert can_borrow(3, 0, "student") is False
    assert can_borrow(9, 0, "faculty") is True
    assert can_borrow(10, 0, "faculty") is False
    assert can_borrow(0, 101, "student") is False


def test_renewal_decisions():
    assert renewal_status(0, False, 2) == "renewed"
    assert renewal_status(0, False, -1) == "overdue"
    assert renewal_status(2, False, 2) == "limit reached"
    assert renewal_status(0, True, 2) == "denied"
