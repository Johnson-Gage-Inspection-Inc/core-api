from office365.sharepoint.fields.number import FieldNumber as FieldNumber

class FieldCurrency(FieldNumber):
    @property
    def currency_locale_id(self) -> int | None: ...
    @currency_locale_id.setter
    def currency_locale_id(self, value: int) -> None: ...
