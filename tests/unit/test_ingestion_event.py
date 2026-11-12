from datetime import date

import pytest

from data_ingestion_framework.models import IngestionEvent, RunMode


def test_scheduled_event_minimal() -> None:
    event = IngestionEvent(mode=RunMode.SCHEDULED)
    assert event.mode is RunMode.SCHEDULED
    assert event.start_date is None
    assert event.end_date is None
    assert event.datasets is None


def test_scheduled_event_from_json() -> None:
    event = IngestionEvent.model_validate({"mode": "scheduled"})
    assert event.mode is RunMode.SCHEDULED


def test_scheduled_rejects_dates() -> None:
    with pytest.raises(ValueError, match="scheduled mode must not include"):
        IngestionEvent(
            mode=RunMode.SCHEDULED,
            start_date=date(2026, 1, 1),
            end_date=date(2026, 1, 7),
        )


def test_backfill_event_valid() -> None:
    event = IngestionEvent(
        mode=RunMode.BACKFILL,
        start_date=date(2020, 1, 1),
        end_date=date(2020, 12, 31),
        datasets=["exchange_rates_a"],
    )
    assert event.datasets == ["exchange_rates_a"]


def test_backfill_requires_dates() -> None:
    with pytest.raises(
        ValueError, match="backfill mode requires start_date and end_date"
    ):
        IngestionEvent(mode=RunMode.BACKFILL)


def test_backfill_rejects_inverted_dates() -> None:
    with pytest.raises(
        ValueError, match="start_date must be less than or equal to end_date"
    ):
        IngestionEvent(
            mode=RunMode.BACKFILL,
            start_date=date(2020, 12, 31),
            end_date=date(2020, 1, 1),
        )
