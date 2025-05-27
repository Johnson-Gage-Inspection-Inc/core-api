from marshmallow import Schema, fields
from qualer_sdk.models.qualer_api_models_asset_to_asset_response_model import QualerApiModelsAssetToAssetResponseModel

# Basic mapping from swagger type string to Marshmallow field
type_mapping = {
    'str': fields.String,
    'int': fields.Integer,
    'float': fields.Float,
    'bool': fields.Boolean,
    'datetime': fields.DateTime,
    'date': fields.Date,
    # Fallback type
    'object': fields.Raw,
}

def generate_schema_from_swagger(model_cls):
    schema_fields = {}
    for attr_name, swagger_type in model_cls.swagger_types.items():
        field_class = type_mapping.get(swagger_type, fields.Raw)
        schema_fields[attr_name] = field_class(allow_none=True)
    return type(f"{model_cls.__name__}Schema", (Schema,), schema_fields)

AssetToAssetSchema = generate_schema_from_swagger(QualerApiModelsAssetToAssetResponseModel)

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
