"""Property-based input-validation tests for processor.py."""
from hypothesis import given, settings, strategies as st
import pytest

from processor import can_borrow, late_fine, renewal_status

SCALARS = st.one_of(
    st.none(), st.booleans(), st.integers(), st.floats(allow_nan=True),
    st.text(), st.binary(), st.lists(st.integers()), st.dictionaries(st.text(), st.integers()),
)
MEMBERS = st.sampled_from(["student", "faculty", "guest"])


@given(member=SCALARS, days=SCALARS, damaged=SCALARS)
@settings(max_examples=200)
def test_late_fine_rejects_malformed_inputs(member, days, damaged):
    valid = member in ("student", "faculty", "guest") and type(days) is int and days >= 0 and type(damaged) is bool
    if valid:
        result = late_fine(member, days, damaged)
        assert type(result) is int and result >= 0
    else:
        with pytest.raises(ValueError):
            late_fine(member, days, damaged)


@given(books=SCALARS, fine=SCALARS, member=SCALARS)
@settings(max_examples=200)
def test_can_borrow_rejects_malformed_inputs(books, fine, member):
    valid = type(books) is int and books >= 0 and type(fine) is int and fine >= 0 and member in ("student", "faculty", "guest")
    if valid:
        assert type(can_borrow(books, fine, member)) is bool
    else:
        with pytest.raises(ValueError):
            can_borrow(books, fine, member)


@given(renewed=SCALARS, reserved=SCALARS, days_left=SCALARS)
@settings(max_examples=200)
def test_renewal_status_rejects_malformed_inputs(renewed, reserved, days_left):
    valid = type(renewed) is int and renewed >= 0 and type(reserved) is bool and type(days_left) is int
    if valid:
        assert renewal_status(renewed, reserved, days_left) in {"denied", "limit reached", "overdue", "renewed"}
    else:
        with pytest.raises(ValueError):
            renewal_status(renewed, reserved, days_left)
