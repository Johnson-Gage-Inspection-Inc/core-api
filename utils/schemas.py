from dataclasses import dataclass, field
from typing import List

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

# Cache for generated schemas to prevent infinite recursion
_schema_cache = {}

# Basic mapping from swagger type string to Marshmallow field
type_mapping = {
    "str": fields.String,
    "int": fields.Integer,
    "float": fields.Float,
    "bool": fields.Boolean,
    "datetime": fields.String,
    "date": fields.Date,
    # Fallback type
    "object": fields.Raw,
}


def generate_schema_from_swagger(model_cls: type) -> type[Schema]:
    """
    Generate a Marshmallow schema class from a Qualer SDK model class.
    This function creates a schema class dynamically based on the model's
    swagger_types mapping, allowing it to handle both single objects and lists
    of objects.

    Args:
        model_cls (type): The Qualer SDK model class to generate the schema from.
    Returns:
        type[Schema]: A Marshmallow schema class that can serialize/deserialize
                      instances of the given model class.
    """
    model_name = model_cls.__name__

    # Return cached schema if already generated
    if model_name in _schema_cache:
        return _schema_cache[model_name]

    schema_fields = {}
    for attr_name, swagger_type in model_cls.swagger_types.items():
        # Handle list types
        if swagger_type.startswith("list["):
            schema_fields[attr_name] = fields.List(fields.Raw(), allow_none=True)
        # Handle all other types using type_mapping or fallback to Raw
        else:
            marshmallow_field = type_mapping.get(swagger_type, fields.Raw)
            schema_fields[attr_name] = marshmallow_field(
                allow_none=True
            )  # Create schema class with fields first
    schema_class = type(f"{model_name}Schema", (Schema,), schema_fields)

    def dump_override(self, obj, *, many=None, **kwargs):
        """Override dump to handle SDK model objects"""

        # Use schema's many setting if dump's many parameter is None
        if many is None:
            many = getattr(self, "many", False)

        if many:
            # Handle list of objects
            converted_objects = []
            for item in obj:
                if hasattr(item, "to_dict") and callable(getattr(item, "to_dict")):
                    converted_objects.append(item.to_dict())
                else:
                    converted_objects.append(item)
            return super(schema_class, self).dump(
                converted_objects, many=True, **kwargs
            )
        else:
            # Handle single object
            if hasattr(obj, "to_dict") and callable(getattr(obj, "to_dict")):
                obj = obj.to_dict()
            return super(schema_class, self).dump(obj, many=False, **kwargs)

    # Add the dump method after schema_class is defined
    schema_class.dump = dump_override
    # Cache and return the schema class
    _schema_cache[model_name] = schema_class

    return schema_class


AssetToAssetSchema = generate_schema_from_swagger(
    QualerApiModelsAssetToAssetResponseModel
)
EmployeeResponseSchema = generate_schema_from_swagger(
    QualerApiModelsClientsToEmployeeResponseModel
)
ClientCompanyResponseSchema = generate_schema_from_swagger(
    QualerApiModelsClientsToClientCompanyResponseModel
)
AssetServiceRecordResponseSchema = generate_schema_from_swagger(
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

    def update(self, other: "WireSetCertResult"):
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
    def normalize_dates(self, data, **kwargs):
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
    def flatten_nested_fields(self, data, **kwargs):
        """Extract nested fields from `file` and `parentReference`."""
        data["mimeType"] = data.get("file", {}).get("mimeType")
        parent = data.get("parentReference", {})
        data["driveId"] = parent.get("driveId")
        data["path"] = parent.get("path")
        return data
        return data
        return data
