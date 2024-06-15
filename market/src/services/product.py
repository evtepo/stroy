import logging
from uuid import UUID

from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.product import Product, Category
from schemas.product import ProductCreate, ProductDelete, ProductUpdate


async def get_all_products(page: int, size: int, category: str, db: AsyncSession) -> list[Product | None]:
    if category:
        query = (
            select(Product)
            .join(Category)
            .offset((page - 1) * size)
            .limit(size)
            .where(Category.name == category)
        )
    else:
        query = select(Product).offset((page - 1) * size).limit(size)

    result = await db.execute(query)

    return result.scalars().all()


async def get_single_product(product_id: UUID, db: AsyncSession) -> Product | None:
    query = select(Product).where(Product.id == product_id)
    result = await db.execute(query)

    return result.scalar_one_or_none()


async def new_product(product: ProductCreate, db: AsyncSession):
    query = select(Category).where(product.category == Category.name)
    result = await db.execute(query)
    category = result.scalar_one_or_none()
    if category:
        try:
            product = Product(
                name=product.name,
                description=product.description,
                price=product.price,
                category=category.name,
            )
            db.add(product)
            await db.commit()

            return product

        except Exception as ex:
            logging.error(f"Failed to create product: {ex}")
            return None

    return None


async def update_product_by_id(product: ProductUpdate, db: AsyncSession):
    if product.category:
        category_query = select(Category).where(Category.name == product.category)
        result = await db.execute(category_query)
        category = result.scalar_one_or_none()

        if not category:
            return JSONResponse(
                {"msg": "Wrong category name."},
                status_code=status.HTTP_400_BAD_REQUEST,
            )

    product_query = select(Product).where(Product.id == product.id)
    result = await db.execute(product_query)
    product_object = result.scalar_one_or_none()
    if not product_object:
        return JSONResponse(
            {"msg": "Wrong project id."},
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    
    for key, value in product.__dict__.items():
        if value is not None:
            setattr(product_object, key, value)

    await db.commit()

    return product_object


async def delete_product_by_id(product: ProductDelete, db: AsyncSession):
    query = select(Product).where(Product.id == product.id)
    result = await db.execute(query)
    product_object = result.scalar_one_or_none()
    if not product_object:
        return JSONResponse(
            {"msg": "Wrong product id."},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    await db.delete(product_object)
    await db.commit()

    return {"msg": "Product successfully deleted."}
