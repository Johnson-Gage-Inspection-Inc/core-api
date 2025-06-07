from office365.sharepoint.fields.multi_choice import (
    FieldMultiChoice as FieldMultiChoice,
)

class FieldRatingScale(FieldMultiChoice):
    @property
    def grid_start_number(self) -> int | None: ...
    @grid_start_number.setter
    def grid_start_number(self, value: int) -> None: ...
    @property
    def range_count(self) -> int | None: ...
