from uuid import UUID

from pydantic import BaseModel, Field


class MixinCategory(BaseModel):
    name: str


class Category(MixinCategory):
    id: UUID

    class Config:
        orm_mode = True


class GetCategory(MixinCategory): ...


class CreateCategory(MixinCategory): ...


class UpdateCategory(MixinCategory):
    new_name: str


class DeleteCategory(MixinCategory): ...
