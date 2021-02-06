Это приложение позволяет создавать напоминания о ваших заплонированных событиях с возможностью уведомления по 
электронной почте. Вы также можете получить список полный список событий за указанный период и список праздников 
той страны, которую вы указали при регистрации.

## Как использовать: 

### 1. Для регистрации ("https://michail.ololosha.xyz/event/register/")
~~~
from requests import post
data = {
    "username": "username",
    "email": "email@email.com",
    "password": "password",
    "country": 19
}
response = post("https://michail.ololosha.xyz/event/register/", data=data)
Сountry от 1 до 222 (19 это Belarus)
~~~
### 2. Для логина и получения токина на почту ("https://michail.ololosha.xyz/event/login/")
~~~
from requests import post
data = {
    "username": "username",
    "email": "email@email.com",
    "password": "password"
}
response = post("https://michail.ololosha.xyz/event/login/", data=data)
~~~
### 3. Для того чтобы создать  событие ('https://michail.ololosha.xyz/event/createevent/')
~~~
from requests import post
from datetime import timedelta
headers = {'Authorization': "Token здесь ваш токен из почты"}
data = {
    "title": "Event",
    "date_start": "2021-02-06T14:35:00Z",
    "date_finish": "2021-02-06T15:25:00Z",
    "reminder": timedelta(seconds=7200),
    "notification": True
}
response = post('https://michail.ololosha.xyz/event/createevent/', headers=headers, data=data)
"date_finish", "reminder", "notification" - не обязательные поля для заполнения
timedelta(seconds=3600), "За час",
timedelta(seconds=7200), "За 2 часа",
timedelta(seconds=14 400), "За 4 часа",
timedelta(seconds=86400), "За день",
timedelta(seconds=604800), "За неделю"
~~~
### 4. Для того что бы посмотреть списков событий ('https://michail.ololosha.xyz/event/listevent/data')
~~~
from requests import get
headers = {'Authorization': "Token здесь ваш токен из почты"}
response = get('https://michail.ololosha.xyz/event/listevent/data/', headers=headers)
response.json()
Для получения списка событий за год в место data укажи год (2021)
Для получения списка событий за месяц в место data укажи год и месяц (2021-01)
Для получения списка событий за день в место data укажи год-месяц-день (2021-01-01)
~~~
### 5. Для того что бы посмотреть списков праздников ('https://michail.ololosha.xyz/event/listholidays/data')
~~~
from requests import get
headers = {'Authorization': "Token здесь ваш токен из почты"}
response = get('https://michail.ololosha.xyz/event/listholidays/?search=2021-01', headers=headers)
response.json()
Для получения списка праздников за год (search=2021)
Для получения списка праздников за месяц (search=2021-01)
~~~

