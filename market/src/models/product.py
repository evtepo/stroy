import uuid

from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.dialects.postgresql import UUID

from storage.db import Base


class Mixin:
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )

    class Config:
        abstract = True


class Product(Mixin, Base):
    __tablename__ = "product"

    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Numeric(10, 2), nullable=False)
    category = Column(
        String,
        ForeignKey("category.name", ondelete="CASCADE"),
        nullable=False,
    )


class Category(Mixin, Base):
    __tablename__ = "category"

    name = Column(String(100), nullable=False, unique=True)
