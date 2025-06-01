from marshmallow import Schema, fields
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
    Generate Marshmallow schemas from Qualer SDK model classes.
    Creates schemas that can serialize SDK objects directly using their to_dict() method.
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
