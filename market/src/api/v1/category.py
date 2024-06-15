from fastapi import APIRouter, Depends, Query, status 
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.category import (
    Category,
    CreateCategory,
    DeleteCategory,
    UpdateCategory,
)
from services.category import (
    get_all_categories,
    get_category,
    new_category,
    delete_category_by_name,
    update_category_by_name,
)
from storage.db import get_session


router = APIRouter()


@router.get(
    "/",
    response_model=list[Category | None],
    summary="Get all categories",
    status_code=status.HTTP_200_OK,
)
async def get_categories(
    page: int = Query(default=1, ge=1, description="Page number"),
    size: int = Query(default=10, ge=10, le=50, description="Page size"),
    db: AsyncSession = Depends(get_session),
):
    result = await get_all_categories(page, size, db)

    return result


@router.get(
    "/{category_name}",
    response_model=Category,
    summary="Get one category.",
    status_code=status.HTTP_200_OK,
)
async def get_single_category(category_name: str, db: AsyncSession = Depends(get_session)):
    result = await get_category(category_name, db)
    if not result:
        return JSONResponse(
            {"msg": "Name error."},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return result


@router.post(
    "/",
    response_model=Category | None,
    summary="Create a new category.",
    status_code=status.HTTP_201_CREATED,
)
async def create_category(category: CreateCategory, db: AsyncSession = Depends(get_session)):
    result = await new_category(category, db)
    if not result:
        return JSONResponse(
            {"msg": "Category already exists"},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return result


@router.patch(
    "/",
    response_model=Category,
    summary="Update category.",
    status_code=status.HTTP_200_OK,
)
async def update_category(category: UpdateCategory, db: AsyncSession = Depends(get_session)):
    result = await update_category_by_name(category, db)
    if not result:
        return JSONResponse(
            {"msg": "Name error."},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return result


@router.delete(
    "/",
    response_model=dict,
    summary="Delete category.",
    status_code=status.HTTP_200_OK,
)
async def delete_category(category: DeleteCategory, db: AsyncSession = Depends(get_session)):
    result = await delete_category_by_name(category, db)
    if not result:
        return JSONResponse(
            {"msg": "Name error."},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return result
