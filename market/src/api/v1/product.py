from uuid import UUID

from fastapi import APIRouter, Depends, status, Query
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.product import (
    ProductCreate,
    ProductDelete,
    ProductResponse,
    ProductUpdate,
)
from services.product import (
    delete_product_by_id,
    get_all_products,
    get_single_product,
    new_product,
    update_product_by_id,
)
from storage.db import get_session


router = APIRouter()


@router.get(
    "/",
    response_model=list[ProductResponse | None],
    summary="Get all products",
    status_code=status.HTTP_200_OK,
)
async def get_products(
    page: int = Query(default=1, ge=1, description="Page number"),
    size: int = Query(default=10, ge=10, le=50, description="Page size"),
    category: str = Query(default=None, description="Product category"),
    db: AsyncSession = Depends(get_session),
):
    return await get_all_products(page, size, category, db)


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
    summary="Get one product.",
    status_code=status.HTTP_200_OK,
)
async def get_product(product_id: UUID, db: AsyncSession = Depends(get_session)):
    result = await get_single_product(product_id, db)
    if not result:
        return JSONResponse(
            {"msg": "Wrong product id."},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return result


@router.post(
    "/",
    response_model=ProductResponse,
    summary="Create a new product.",
    status_code=status.HTTP_201_CREATED,
)
async def create_product(product: ProductCreate, db: AsyncSession = Depends(get_session)):
    result = await new_product(product, db)
    if not result:
        return JSONResponse(
            {"msg": "Something went wrong. Wrong data."},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    return result


@router.patch(
    "/",
    response_model=ProductResponse,
    summary="Update product.",
    status_code=status.HTTP_200_OK,
)
async def update_product(product: ProductUpdate, db: AsyncSession = Depends(get_session)):
    return await update_product_by_id(product, db)


@router.delete(
    "/",
    response_model=dict,
    summary="Delete product.",
    status_code=status.HTTP_200_OK,
)
async def delete_product(product: ProductDelete, db: AsyncSession = Depends(get_session)):
    return await delete_product_by_id(product, db)
