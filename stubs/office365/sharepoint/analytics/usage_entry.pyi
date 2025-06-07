from office365.runtime.queries.service_operation import ServiceOperationQuery as ServiceOperationQuery
from office365.sharepoint.entity import Entity as Entity

class AnalyticsUsageEntry(Entity):
    @staticmethod
    def log_analytics_event(context, event_type_id, item_id): ...
    @staticmethod
    def log_analytics_app_event2(context, app_event_type_id, item_id, rollup_scope_id, site_id, user_id): ...
    @property
    def entity_type_name(self): ...
