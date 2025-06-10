from _typeshed import Incomplete
from office365.outlook.calendar.email_address import EmailAddress as EmailAddress
from office365.outlook.mail.automatic_replies_mailtips import (
    AutomaticRepliesMailTips as AutomaticRepliesMailTips,
)
from office365.outlook.mail.tips.error import MailTipsError as MailTipsError
from office365.runtime.client_value import ClientValue as ClientValue

class MailTips(ClientValue):
    automaticReplies: Incomplete
    customMailTip: Incomplete
    deliveryRestricted: Incomplete
    emailAddress: Incomplete
    error: Incomplete
    externalMemberCount: Incomplete
    isModerated: Incomplete
    def __init__(
        self,
        automatic_replies=...,
        custom_mail_tip: Incomplete | None = None,
        delivery_restricted: Incomplete | None = None,
        email_address=...,
        error=...,
        external_member_count: Incomplete | None = None,
        is_moderated: Incomplete | None = None,
    ) -> None: ...
