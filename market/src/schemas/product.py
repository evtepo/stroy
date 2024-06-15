from uuid import UUID

from pydantic import BaseModel


class ProductMixin(BaseModel):
    name: str


class IdMixin(BaseModel):
    id: UUID


class ProductGetSingle(ProductMixin): ...


class ProductCreate(ProductMixin):
    price: float
    description: str | None
    category: str


class ProductResponse(ProductCreate, IdMixin): ...


class ProductUpdate(IdMixin):
    name: str | None
    price: float | None
    description: str | None
    category: str | None


class ProductDelete(IdMixin): ...
