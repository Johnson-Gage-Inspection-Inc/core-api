from _typeshed import Incomplete
from office365.outlook.mail.recipient import Recipient as Recipient
from office365.runtime.client_value import ClientValue as ClientValue
from office365.runtime.client_value_collection import ClientValueCollection as ClientValueCollection
from office365.runtime.types.collections import StringCollection as StringCollection

class MessageRuleActions(ClientValue):
    assignCategories: Incomplete
    copyToFolder: Incomplete
    delete: Incomplete
    forwardAsAttachmentTo: Incomplete
    forwardTo: Incomplete
    markAsRead: Incomplete
    markImportance: Incomplete
    moveToFolder: Incomplete
    permanentDelete: Incomplete
    redirectTo: Incomplete
    stopProcessingRules: Incomplete
    def __init__(self, assign_categories: Incomplete | None = None, copy_to_folder: Incomplete | None = None, delete: Incomplete | None = None, forward_as_attachment_to: Incomplete | None = None, forward_to: Incomplete | None = None, mark_as_read: Incomplete | None = None, mark_importance: Incomplete | None = None, move_to_folder: Incomplete | None = None, permanent_delete: Incomplete | None = None, redirect_to: Incomplete | None = None, stop_processing_rules: Incomplete | None = None) -> None: ...
