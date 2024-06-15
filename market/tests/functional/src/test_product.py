import pytest
import http
from typing import Callable

from settings.settings import product_url
from testdata.product import product, new_price


product_id: str | None = None


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
            product,
            {"status": http.HTTPStatus.CREATED},
        ),
    ],
)
@pytest.mark.asyncio
async def test_create_product(make_request: Callable, query_data: dict, expected_answer: dict):
    """
    Тест создания продукта.
    """
    response: dict = await make_request("POST", product_url, params=query_data)

    global product_id
    product_id = response.get("body").get("id")

    assert response.get("body").get("name") == query_data.get("name")
    assert response.get("status") == expected_answer.get("status")


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
            product,
            {"status": http.HTTPStatus.OK},
        ),
    ],
)
@pytest.mark.asyncio
async def test_update_product(make_request: Callable, query_data: dict, expected_answer: dict):
    """
    Тест изменения продукта.
    """
    global product_id
    query_data["id"] = product_id
    query_data["price"] = new_price

    response: dict = await make_request("PATCH", product_url, params=query_data)

    assert response.get("body").get("name") == query_data.get("name")
    assert response.get("status") == expected_answer.get("status")


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
            product,
            {"status": http.HTTPStatus.OK},
        ),
    ],
)
@pytest.mark.asyncio
async def test_delete_product(make_request: Callable, query_data: dict, expected_answer: dict):
    """
    Тест удаления продукта.
    """
    global product_id
    params = {"id": product_id}
    response: dict = await make_request("DELETE", product_url, params=params)

    assert response.get("status") == expected_answer.get("status")
