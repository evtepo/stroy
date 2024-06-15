import uvicorn
from fastapi import FastAPI

from api.v1.product import router as product_router
from api.v1.category import router as category_router
from configs.documentation import documentation
from configs.settings import settings


app = FastAPI(
    title=settings.project_name,
    **documentation,
)

app.include_router(product_router, prefix="/api/v1/product", tags=["Product"])
app.include_router(category_router, prefix="/api/v1/category", tags=["Category"])


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.localhost,
        port=settings.localport,
    )
