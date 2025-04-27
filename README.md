# Online_store

Проект Интернет-магазина ... на Django.


## Запуск проекта


### Требования
- Python 3.10+
- Django 5.0+


### Установка
1. Клонировать репозиторий:
```
git clone git@github.com:Nefertitu/Online_store.git
```
2. Установите зависимости:
```
poetry install
```
3. Применить миграции:

```
python manage.py migrate
```
4. Запустить сервер:

```
python manage.py runserver
```
Проект будет доступен по адресу: http://127.0.0.1:8000

## Структура проекта
Online_store/
├── config/                 # Основные настройки Django
├── catalog/                # Приложение каталога товаров
│   ├── migrations/       
│   ├── templates/          # Шаблоны
│   │    ├── home.html      # Шаблон страницы `home`
│   │    └── contacts.html  # Шаблон страницы `contscts`
│   ├── models.py           # Модели БД
│   ├── views.py            # Логика страниц
│   ├── urls.py             # Маршруты приложения 
│   ├── admin.py            
│   ├── apps.py             
│   └── tests.py             
├── static/                 # CSS/JS/Изображения
├── .flake8                 
├── .gitignore                 
├── LICENSE.txt                 
├── poetry.lock                
├── pyproject.toml                
├── README.md                
└── manage.py


## Доступные URL-адреса

Главная страница: /home/

Контакты: /contacts/


## Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE.txt).