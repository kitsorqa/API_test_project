from pydantic import BaseModel

class InventoryItemModel(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: str
    complete: bool


class CreatedOrderModel(BaseModel):
    id: int
    petId: int
    quantity: int
    complete: int


class DeletedOrderModel(BaseModel):
    code: int
    type: str
    message: int