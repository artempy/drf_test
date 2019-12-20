Создание приложения:
POST /api/test
Пример тела запроса в json:
{
	"name": "test_app"
}

Возвращает API_KEY, который нужно использовать для дальнейшей работы.


Обновление информации приложения:
PUT /api/test
Пример тела запроса в json:
{
	"API_KEY": "e0c7309b0f4b5ca9c52da5c48343c22d009f827210fd598371262b383e443a49",
	"name": "new_test_app"
}

Удаление приложения:
DELETE /api/test
Пример тела запроса в json:
{
	"API_KEY": "e0c7309b0f4b5ca9c52da5c48343c22d009f827210fd598371262b383e443a49",
}


Получение информации о приложении:
GET /api/test?api_key=YOUR_API_KEY
 
Возвращает json вида:
 {
    "data": {
        "id": 4,
        "name": "test_app",
        "api_key": "e0c7309b0f4b5ca9c52da5c48343c22d009f827210fd598371262b383e443a49"
    },
    "success": true
}


Создать новый ключ API приложения:
POST /api/set_api_key
Пример тела запроса в json:
{
	"API_KEY": "e0c7309b0f4b5ca9c52da5c48343c22d009f827210fd598371262b383e443a49",
}

Возвращает json вида:
{
    "success": true,
    "API_KEY": "ebf751f1b62441146e24a3868856b796ca9a7890cb9037dc9a56e6b17e5b7fd1"
}
