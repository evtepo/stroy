import logging

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.category import (
    CreateCategory,
    DeleteCategory,
    UpdateCategory,
)
from models.product import Category


async def get_all_categories(page: int, size: int, db: AsyncSession) -> list[Category | None]:
    query = select(Category).offset((page - 1) * size).limit(size)
    result = await db.execute(query)
    result = result.scalars().all()
    return result


async def get_category(category_name: str, db: AsyncSession) -> Category | None:
    query = select(Category).where(Category.name == category_name)
    result = await db.execute(query)
    category = result.scalar_one_or_none()

    return category


async def new_category(category_create: CreateCategory, db: AsyncSession) -> Category | None:
    try:
        category = Category(name=category_create.name)
        db.add(category)
        await db.commit()
        return category
    except Exception as ex:
        logging.error(f"Error: {type(ex).__name__} -> {ex}")
        return None


async def update_category_by_name(category_update: UpdateCategory, db: AsyncSession) -> Category | None:
    query = select(Category).where(Category.name == category_update.name)
    result = await db.execute(query)
    category = result.scalar_one_or_none()
    if not category:
        logging.error(
            f"Error: Category doesn't exists. Function name -> {update_category_by_name.__name__}"
        )
        return None

    category.name = category_update.new_name
    await db.commit()
    return category


async def delete_category_by_name(category_delete: DeleteCategory, db: AsyncSession) -> dict | None:
    query = select(Category).where(Category.name == category_delete.name)
    result = await db.execute(query)
    category = result.scalar_one_or_none()
    if not category:
        logging.error(
            f"Error: Category doesn't exists. Function name -> {delete_category_by_name.__name__}"
        )
        return None

    await db.delete(category)
    await db.commit()

    return {"msg": "Category successfully deleted."}
