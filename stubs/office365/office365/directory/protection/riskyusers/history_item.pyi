from office365.directory.protection.riskyusers.activity import (
    RiskUserActivity as RiskUserActivity,
)
from office365.directory.protection.riskyusers.risky_user import RiskyUser as RiskyUser

class RiskyUserHistoryItem(RiskyUser):
    @property
    def activity(self): ...
    @property
    def initiated_by(self) -> str | None: ...
