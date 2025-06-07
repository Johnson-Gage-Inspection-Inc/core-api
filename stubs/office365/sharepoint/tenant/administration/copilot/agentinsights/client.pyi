from office365.runtime.client_result import ClientResult as ClientResult
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.paths.service_operation import ServiceOperationPath as ServiceOperationPath
from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.client_context import ClientContext as ClientContext
from office365.sharepoint.tenant.administration.copilot.agentinsights.report_metadata import SPOCopilotAgentInsightsReportMetadata as SPOCopilotAgentInsightsReportMetadata
from office365.sharepoint.tenant.administration.datagovernance.client_base import SPDataGovernanceRestApiClientBase as SPDataGovernanceRestApiClientBase

class SPOCopilotAgentInsightsRestApiClient(SPDataGovernanceRestApiClientBase):
    def __init__(self, context: ClientContext, authorization_header: str, url: str, user_agent: str) -> None: ...
    def get_all_copilot_agent_insights_reports_metadata(self): ...
