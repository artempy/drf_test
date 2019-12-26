## Развертывание
#### Стандартное:
```
pip -r install requirements.txt  
python manage.py makemigrations app  
python manage.py migrate 
```
Запуск: 
```
python manage.py runserver
```

  
#### Посредством Docker:
```
docker-compose up --build -d  
docker exec -ti djangotestapi_django_1 bash  
python manage.py makemigrations app  
python manage.py migrate  
```
  
  
## Использование
#### Создание приложения:
*POST /api/test*  
  
Пример запроса:  
```
curl -d '{"name": "super"}' -H 'Content-Type: application/json' -X POST http://127.0.0.1:8000/api/test
```

Пример тела запроса в json:  
{  
    "name": "test_app"  
}  
  
Возвращает API_KEY, который нужно использовать для дальнейшей работы.  
Передавать в заголовке **APIKEY**.  
Пример: APIKEY: a41d1a8663b8e4dec488cce676742daa24d7360aad1457296b7937c6241f42c2
  
  
#### Обновление информации приложения:
*PUT /api/test*  
  
Пример запроса:  
```
curl -d '{"name": "super1"}' -H 'Content-Type: application/json'  -H 'APIKEY: a41d1a8663b8e4dec488cce676742daa24d7360aad1457296b7937c6241f42c2' -X PUT http://127.0.0.1:8000/api/test
```
  
Пример тела запроса в json:  
{  
  "name": "new_test_app"  
}  
  
  
#### Удаление приложения:
*DELETE /api/test*  
  
Пример запроса:  
```
curl -H 'Content-Type: application/json'  -H 'APIKEY: a41d1a8663b8e4dec488cce676742daa24d7360aad1457296b7937c6241f42c2' -X DELETE http://127.0.0.1:8000/api/test
```
  
  
#### Получение информации о приложении:  
*GET /api/test*  
  
Пример запроса:  
```
curl -H 'APIKEY: a41d1a8663b8e4dec488cce676742daa24d7360aad1457296b7937c6241f42c2' http://127.0.0.1:8000/api/test
```
   
Возвращает json вида:  
{  
    "data": {  
        "id": 4,  
        "name": "test_app",  
        "api_key": "e0c7309b0f4b5ca9c52da5c48343c22d009f827210fd598371262b383e443a49"  
    },  
    "success": true  
}  
  
  
#### Создать новый ключ API приложения:
*POST /api/set_api_key*  
  
Пример запроса:  
```
curl -H 'Content-Type: application/json'  -H 'APIKEY: a41d1a8663b8e4dec488cce676742daa24d7360aad1457296b7937c6241f42c2' -X POST http://127.0.0.1:8000/api/set_api_key
```
  
Возвращает json вида:  
{  
    "success": true,  
    "API_KEY": "ebf751f1b62441146e24a3868856b796ca9a7890cb9037dc9a56e6b17e5b7fd1"  
}  
