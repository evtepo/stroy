description = """
Movies API позволяет получить данные о произведениях, персонах и жанре произведений.

### Products
* **/api/v1/product**:
    \n\t**1.Получить список продуктов (GET):**
        \n\t\t- Использовать "category" для получения продуктов в категории (Получить его -> GET /api/v1/category/{category_name}).
    \n\t**2.Создание продукта (POST):**
        \n\t\t- Перед созданием нужно создать категорию ->  POST /api/v1/category
    \n\t**3.Обновление продукта (PATCH)**
    \n\t**4.Удаление продутка (DELETE)**
    \n\t**5.Получение конкретного продукта: (GET)**
        \n\t\t- Узнать id продукта -> GET /api/v1/product
### Category
* **/api/v1/category**:
    \n\t**1.Получить список категорий (GET):**
    \n\t**2.Создание категории (POST)**
    \n\t**3.Обновление категории (PATCH)**
    \n\t**4.Удаление категории (DELETE)**
    \n\t**5.Получение конкретной категории: (GET)**
        \n\t\t- Узнать name категории -> GET /api/v1/category

"""

documentation = {
    "description": description,
    "version": "1.0",
}
