from datetime import date

import pytest

from data_ingestion_framework.models import DateRange, RunMode, RunStatus


def test_run_mode_values() -> None:
    assert RunMode.SCHEDULED == "scheduled"
    assert RunMode.BACKFILL == "backfill"


def test_run_status_values() -> None:
    assert RunStatus.RUNNING == "running"
    assert RunStatus.SUCCESS == "success"
    assert RunStatus.FAILED == "failed"


def test_date_range_accepts_equal_bounds() -> None:
    window = DateRange(start=date(2026, 11, 12), end=date(2026, 11, 12))
    assert window.start == window.end


def test_date_range_rejects_inverted_bounds() -> None:
    with pytest.raises(ValueError, match="start must be less than or equal to end"):
        DateRange(start=date(2026, 11, 13), end=date(2026, 11, 12))
