from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    service_protocol: str = Field(alias="FASTAPI_PROTOCOL")
    service_host: str = Field(alias="FASTAPI_HOST")
    service_port: int = Field(alias="FASTAPI_PORT")


settings = Settings()

product_url = f"{settings.service_protocol}://{settings.service_host}:{settings.service_port}/api/v1/product"
category_url = f"{settings.service_protocol}://{settings.service_host}:{settings.service_port}/api/v1/category"
