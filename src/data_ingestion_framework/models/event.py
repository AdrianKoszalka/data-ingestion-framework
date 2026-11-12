"""Lambda / CLI ingestion event contract."""

from datetime import date

from pydantic import BaseModel, model_validator

from data_ingestion_framework.models.enums import RunMode


class IngestionEvent(BaseModel):
    """Input contract for scheduled and backfill runs."""

    mode: RunMode
    start_date: date | None = None
    end_date: date | None = None
    datasets: list[str] | None = None

    @model_validator(mode="after")
    def validate_mode_fields(self) -> "IngestionEvent":
        if self.mode is RunMode.SCHEDULED:
            if self.start_date is not None or self.end_date is not None:
                raise ValueError(
                    "scheduled mode must not include start_date or end_date"
                )
            return self

        if self.start_date is None or self.end_date is None:
            raise ValueError("backfill mode requires start_date and end_date")
        if self.start_date > self.end_date:
            raise ValueError("start_date must be less than or equal to end_date")
        return self
