from office365.directory.policies.base import PolicyBase as PolicyBase
from office365.directory.policies.template import PolicyTemplate as PolicyTemplate
from office365.runtime.paths.resource_path import ResourcePath as ResourcePath
from office365.runtime.types.collections import StringCollection as StringCollection

class CrossTenantAccessPolicy(PolicyBase):
    @property
    def allowed_cloud_endpoints(self): ...
    def templates(self) -> PolicyTemplate: ...
