from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.paths.service_operation import ServiceOperationPath as ServiceOperationPath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.tenant.administration.datagovernance.client_base import SPDataGovernanceRestApiClientBase as SPDataGovernanceRestApiClientBase
from office365.sharepoint.tenant.administration.datagovernance.insight_metadata import SPDataGovernanceInsightMetadata as SPDataGovernanceInsightMetadata

class SPDataGovernanceInsightRestApiClient(SPDataGovernanceRestApiClientBase):
    def __init__(self, context: ClientContext, authorization_header: str, url: str, user_agent: str) -> None: ...
    def create_data_access_governance_report(self, report_entity, workload, report_type, file_sensitivity_label_name, file_sensitivity_label_guid, name, template, privacy, site_sensitivity_label_guid, count_of_users_more_than): ...
    def export_spo_data_access_governance_insight(self, report_id): ...
