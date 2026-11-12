"""Shared enums for ingestion runs."""

from enum import StrEnum


class RunMode(StrEnum):
    """How an ingestion run was triggered."""

    SCHEDULED = "scheduled"
    BACKFILL = "backfill"


class RunStatus(StrEnum):
    """Lifecycle status of a run or backfill record."""

    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
