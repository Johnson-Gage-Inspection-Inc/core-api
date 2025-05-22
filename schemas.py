from marshmallow import Schema, fields

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
