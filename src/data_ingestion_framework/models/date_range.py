"""Inclusive calendar date range."""

from datetime import date

from pydantic import BaseModel, model_validator


class DateRange(BaseModel):
    """Inclusive date window: both start and end are included."""

    start: date
    end: date

    @model_validator(mode="after")
    def start_must_precede_end(self) -> "DateRange":
        if self.start > self.end:
            raise ValueError("start must be less than or equal to end")
        return self
