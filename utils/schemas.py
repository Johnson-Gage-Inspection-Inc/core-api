import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Pattern

from marshmallow import EXCLUDE, Schema, fields, pre_load
from qualer_sdk.models.qualer_api_models_asset_service_records_to_asset_service_record_response_model import (
    QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel,
)
from qualer_sdk.models.qualer_api_models_asset_to_asset_response_model import (
    QualerApiModelsAssetToAssetResponseModel,
)
from qualer_sdk.models.qualer_api_models_clients_to_client_company_response_model import (
    QualerApiModelsClientsToClientCompanyResponseModel,
)
from qualer_sdk.models.qualer_api_models_clients_to_employee_response_model import (
    QualerApiModelsClientsToEmployeeResponseModel,
)

from utils.pydantic_to_marshmallow import pydantic_to_marshmallow


class WorkItemNumber(str):
    """
    Custom Marshmallow Field for work item numbers.
    Normalizes by adding '56561-' prefix if missing, then validates format.
    Allowed formats (after prefix):
      - 56561-XXXXXX
      - 56561-XXXXXX.XX
      - 56561-XXXXXX-YY
      - 56561-XXXXXX.XX-YY
      - optionally followed by a revision: R1 , R2,...
    """

    def __new__(cls, value: str) -> "WorkItemNumber":
        """Create a new WorkItemNumber instance.

        Args:
            value (str): The work item number string.

        Raises:
            TypeError: If value is not a string.
            ValueError: If value is not a valid work item number.

        Returns:
            WorkItemNumber: The validated work item number.
        """
        WORK_ITEM_PATTERN: Pattern[str] = re.compile(
            r"^56561-\d{6}(?:\.\d{2})?(?:-\d{2})?(?:R\d{1,2})?$"
        )

        if not isinstance(value, str):
            raise TypeError("WorkItemNumber must be created from a string")
        # Normalize prefix if missing
        normalized: str = value if value.startswith("56561-") else f"56561-{value}"
        if not WORK_ITEM_PATTERN.fullmatch(normalized):
            raise ValueError(
                f"Invalid WorkItemNumber: {value!r}. "
                "Expected formats like '56561-123456', '56561-123456.78', "
                "'56561-123456-90', '56561-123456.78-90', optionally followed by 'R1' or 'R12'."
            )
        # Create the str instance
        return str.__new__(cls, normalized)


AssetToAssetSchema = pydantic_to_marshmallow(QualerApiModelsAssetToAssetResponseModel)
EmployeeResponseSchema = pydantic_to_marshmallow(
    QualerApiModelsClientsToEmployeeResponseModel
)
ClientCompanyResponseSchema = pydantic_to_marshmallow(
    QualerApiModelsClientsToClientCompanyResponseModel
)
AssetServiceRecordResponseSchema = pydantic_to_marshmallow(
    QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel
)


class WorkItemDetailsQuerySchema(Schema):
    workItemNumber = fields.Str(required=True)


class WorkItemDetailsSchema(Schema):
    clientCompanyId = fields.Int(required=True)
    serviceOrderId = fields.Int(required=True)
    assetId = fields.Int(required=True)
    certificateNumber = fields.Str()
    assetName = fields.Str()
    assetMaker = fields.Str()
    assetTag = fields.Str()
    serialNumber = fields.Str()
    manufacturerPartNumber = fields.Str()
    categoryName = fields.Str()
    rootCategoryName = fields.Str()
    productManufacturer = fields.Str()
    productName = fields.Str()
    purchaseOrderNumber = fields.Str()
    assetAttributes = fields.Dict()


class WhoamiResponse(Schema):
    user = fields.String(required=True)
    sub = fields.String(required=True)


class DaqbookOffsetSchema(Schema):
    """Schema for daqbook offset calibration data."""

    tn = fields.String(
        required=True, metadata={"description": "Test number/daqbook identifier"}
    )
    temp = fields.Float(
        required=True, metadata={"description": "Temperature point in degrees"}
    )
    point = fields.Integer(
        required=True, metadata={"description": "Measurement point number (1-40)"}
    )
    reading = fields.Float(
        required=True, metadata={"description": "Offset reading value"}
    )


class WireOffsetSchema(Schema):
    """Schema for wire offset correction factors"""

    class Meta:
        unknown = EXCLUDE

    id = fields.Integer(dump_only=True)
    traceability_no = fields.String(
        required=True, metadata={"description": "Wire lot identifier (e.g., '072513A')"}
    )
    nominal_temp = fields.Decimal(
        required=True, metadata={"description": "Temperature in Celsius"}
    )
    correction_factor = fields.Decimal(
        required=True, metadata={"description": "Wire correction factor"}
    )
    created_at = fields.DateTime(
        dump_only=True, metadata={"description": "When this record was created"}
    )
    updated_at = fields.DateTime(
        dump_only=True, metadata={"description": "When this record was last updated"}
    )
    updated_by = fields.String(
        allow_none=True,
        metadata={"description": "SharePoint user who last modified the source file"},
    )


@dataclass
class WireSetCertResult:
    """Data class to hold the result of the refresh operation."""

    status: str
    message: str = ""
    records_processed: int = 0
    records_added: int = 0
    records_updated: int = 0
    errors: List[str] = field(default_factory=list)

    def update(self, other: "WireSetCertResult") -> None:
        """
        Update this result with another WireSetCertResult.

        Args:
            other: Another WireSetCertResult to merge into this one
        """
        self.status = other.status
        self.message = other.message
        self.records_processed += other.records_processed
        self.records_added += other.records_added
        self.records_updated += other.records_updated
        self.errors.extend(other.errors)


class WireSetCertSchema(Schema):
    """Schema for wire set certificate mappings"""

    class Meta:
        unknown = EXCLUDE

    id = fields.Integer(dump_only=True)
    serial_number = fields.String(required=True)
    wire_set_group = fields.String(required=True)

    asset_id = fields.Integer(allow_none=True)
    asset_tag = fields.String(allow_none=True)
    custom_order_number = fields.String(allow_none=True)

    service_date = fields.DateTime(allow_none=True)
    next_service_date = fields.DateTime(allow_none=True)

    certificate_number = fields.String(allow_none=True)
    wire_roll_cert_number = fields.String(allow_none=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    @pre_load
    def normalize_dates(self, data: dict, **kwargs: dict) -> dict:
        for fld in ("service_date", "next_service_date"):
            val = data.get(fld)
            # pandas.Timestamp or numpy datetime64
            if hasattr(val, "to_pydatetime"):
                # Convert to ISO string: "2025-01-15T00:00:00"
                data[fld] = val.to_pydatetime().isoformat()
        return data


# SharePoint Integration Schemas
class SharePointFileReferenceSchema(Schema):
    """Schema for SharePoint file reference responses."""

    id = fields.String(allow_none=True, metadata={"description": "SharePoint file ID"})
    name = fields.String(allow_none=True, metadata={"description": "File name"})
    webUrl = fields.String(
        allow_none=True, metadata={"description": "SharePoint web URL for the file"}
    )
    downloadUrl = fields.String(
        allow_none=True, metadata={"description": "Temporary download URL"}
    )
    size = fields.Integer(
        allow_none=True, metadata={"description": "File size in bytes"}
    )
    lastModified = fields.String(
        allow_none=True, metadata={"description": "Last modified timestamp"}
    )
    mimeType = fields.String(
        allow_none=True, metadata={"description": "MIME type of the file"}
    )
    driveId = fields.String(
        allow_none=True, metadata={"description": "SharePoint drive ID"}
    )
    path = fields.String(
        allow_none=True, metadata={"description": "File path within the drive"}
    )


class SharePointFileSearchQuerySchema(Schema):
    """Schema for SharePoint file search requests."""

    query = fields.String(
        required=True,
        metadata={"description": "Search query for finding files in SharePoint"},
    )


class SharePointFolderContentsQuerySchema(Schema):
    """Schema for SharePoint folder listing requests."""

    folderPath = fields.String(
        required=False,
        load_default="",
        metadata={"description": "Path to folder within the drive (empty for root)"},
    )


class SharePointFileInfoSchema(Schema):
    """Schema for SharePoint file metadata from the Graph API."""

    class Meta:
        unknown = EXCLUDE  # Ignore extra fields not defined below

    # Top-level fields
    id = fields.String(required=True)
    name = fields.String(required=True)
    webUrl = fields.String(required=True)
    size = fields.Integer(required=True)
    lastModifiedDateTime = fields.String(required=True)
    downloadUrl = fields.String(required=True, data_key="@microsoft.graph.downloadUrl")

    # Flattened from nested objects via @pre_load
    mimeType = fields.String(required=True)
    driveId = fields.String(required=True)
    path = fields.String(required=True)

    @pre_load
    def flatten_nested_fields(
        self, data: Dict[str, Any], **kwargs: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Extract nested fields from `file` and `parentReference`."""
        data["mimeType"] = data.get("file", {}).get("mimeType")
        parent = data.get("parentReference", {})
        data["driveId"] = parent.get("driveId")
        data["path"] = parent.get("path")
        return data
