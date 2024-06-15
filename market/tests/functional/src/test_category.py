import pytest
import http
from typing import Callable

from settings.settings import category_url
from testdata.category import category1, category2, category2_new_name



@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
            category1,
            {"status": http.HTTPStatus.CREATED},
        ),
        (
            category2,
            {"status": http.HTTPStatus.CREATED},
        ),
    ],
)
@pytest.mark.asyncio
async def test_create_category(make_request: Callable, query_data: dict, expected_answer: dict):
    """
    Тест создания категории.
    """
    response: dict = await make_request("POST", category_url, params=query_data)

    assert response.get("body").get("name") == query_data.get("name")
    assert response.get("status") == expected_answer.get("status")


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
            {"page": 1, "size": 10},
            {"status": http.HTTPStatus.OK, "length": 2},
        ),
    ],
)
@pytest.mark.asyncio
async def test_get_category(make_request: Callable, query_data: dict, expected_answer: dict):
    """
    Тест получения списка категорий.
    """
    response: dict = await make_request("GET", category_url, params=query_data)

    assert expected_answer.get("status") == response.get("status")
    assert expected_answer.get("length") == len(response.get("body"))


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
            category2_new_name,
            {"status": http.HTTPStatus.OK},
        ),
    ],
)
@pytest.mark.asyncio
async def test_update_category(make_request: Callable, query_data: dict, expected_answer: dict):
    """
    Тест изменения категории.
    """
    response: dict = await make_request("PATCH", category_url, params=query_data)

    assert response.get("status") == expected_answer.get("status")


@pytest.mark.parametrize(
    "query_data, expected_answer",
    [
        (
            {"name": category2_new_name.get("new_name")},
            {"status": http.HTTPStatus.OK},
        ),
    ],
)
@pytest.mark.asyncio
async def test_delete_category(make_request: Callable, query_data: dict, expected_answer: dict):
    """
    Тест удаления категории.
    """
    print(query_data)
    response: dict = await make_request("DELETE", category_url, params=query_data)

    assert response.get("status") == expected_answer.get("status")
