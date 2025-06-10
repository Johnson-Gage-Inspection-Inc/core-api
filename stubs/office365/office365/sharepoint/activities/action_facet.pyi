from _typeshed import Incomplete
from office365.runtime.client_value import ClientValue as ClientValue
from office365.sharepoint.activities.facets.add_to_onedrive import (
    AddToOneDriveFacet as AddToOneDriveFacet,
)
from office365.sharepoint.activities.facets.checkin import CheckinFacet as CheckinFacet
from office365.sharepoint.activities.facets.checkout import (
    CheckoutFacet as CheckoutFacet,
)
from office365.sharepoint.activities.facets.create import CreateFacet as CreateFacet
from office365.sharepoint.activities.facets.delete import DeleteFacet as DeleteFacet
from office365.sharepoint.activities.facets.discard_checkout import (
    DiscardCheckoutFacet as DiscardCheckoutFacet,
)
from office365.sharepoint.activities.facets.edit import EditFacet as EditFacet
from office365.sharepoint.activities.facets.get_comment import (
    GetCommentFacet as GetCommentFacet,
)
from office365.sharepoint.activities.facets.get_mention import (
    GetMentionFacet as GetMentionFacet,
)
from office365.sharepoint.activities.facets.move import MoveFacet as MoveFacet
from office365.sharepoint.activities.facets.point_in_time_restore import (
    PointInTimeRestoreFacet as PointInTimeRestoreFacet,
)
from office365.sharepoint.activities.facets.rename import RenameFacet as RenameFacet
from office365.sharepoint.activities.facets.sharing import SharingFacet as SharingFacet
from office365.sharepoint.activities.facets.task_completed import (
    TaskCompletedFacet as TaskCompletedFacet,
)
from office365.sharepoint.activities.facets.version import VersionFacet as VersionFacet

class ActionFacet(ClientValue):
    addToOneDrive: Incomplete
    checkin: Incomplete
    checkout: Incomplete
    comment: Incomplete
    create: Incomplete
    delete: Incomplete
    discardCheckout: Incomplete
    edit: Incomplete
    mention: Incomplete
    move: Incomplete
    pointInTimeRestore: Incomplete
    rename: Incomplete
    share: Incomplete
    taskCompleted: Incomplete
    version: Incomplete
    def __init__(
        self,
        add_to_one_drive=...,
        checkin=...,
        checkout=...,
        comment=...,
        create=...,
        delete=...,
        discard_checkout=...,
        edit=...,
        mention=...,
        move=...,
        pointInTimeRestore=...,
        rename=...,
        share=...,
        taskCompleted=...,
        version=...,
    ) -> None: ...
    @property
    def facet_type(self): ...
    @property
    def entity_type_name(self): ...
