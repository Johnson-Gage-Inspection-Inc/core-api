class AzureEnvironment:
    Global: str
    USGovernment: str
    USGovernmentHigh: str
    China: str
    Germany: str
    USGovernmentDoD: str
    @classmethod
    def get_graph_authority(cls, env: str) -> str: ...
    @classmethod
    def get_login_authority(cls, env: str) -> str: ...
