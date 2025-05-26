# Online_store

Проект Интернет-магазина по продаже комнатных растений на Django.


## Запуск проекта

### Требования
- Python 3.10+
- Django 5.0+

### Установка
1. Подготовка базы данных (`PostgreSQL`):
Перед запуском проекта создайте БД:
```
sudo -u postgres psql -c "CREATE DATABASE your_db_name;"
sudo -u postgres psql -c "CREATE USER your_db_user WITH PASSWORD 'your_db_password';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;"
```
2. Клонировать репозиторий:
```
git clone git@github.com:Nefertitu/Online_store.git
cd Online_store
```
3. Настройка окружения:

Создайте файл .env на основе шаблона (`.env.sample`):
```
cp .env.sample .env
```
Отредактируйте .env (укажите свои секретные ключи, настройки БД и т.д.)

4. Установка зависимостей:
```
poetry install
```
5. Миграции базы данных:
```
python manage.py migrate
```
6. Создание суперпользователя (для доступа в админ-панель):
```
python manage.py createsuperuser
```
Следуйте инструкциям в терминале, чтобы задать логин/пароль.

7. Загрузка тестовых данных (опционально):
```
python manage.py add_products
```
8. Запуск сервера:
```
python manage.py runserver
```
После запуска откройте в браузере:

[Админ-панель]: http://127.0.0.1:8000/admin/

[Главная страница]: http://127.0.0.1:8000/catalog/

[Контакты]: http://127.0.0.1:8000/catalog/contacts/

[Страница с информацией о товаре]: http://127.0.0.1:8000/catalog/id/

[Добавить товар]: http://127.0.0.1:8000/catalog/create/

[Редактировать товар]: http://127.0.0.1:8000/catalog/id/update/

[Удалить товар]: http://127.0.0.1:8000/catalog/id/delete/

[Страница Блог(Blog)]: http://127.0.0.1:8000/blogs/

[Посмотреть пост]: http://127.0.0.1:8000/blogs/id/

[Редактировать пост]: http://127.0.0.1:8000/blogs/id/update/

[Удалить пост]: http://127.0.0.1:8000/blogs/id/delete/


## Структура проекта
Online_store/
├── config/                         # Основные настройки Django
├── blog/                           # Приложение blog
│   ├── migrations/                 # Директория для файлов миграции
│   ├── templates/                  # Шаблоны
│   │    └── blog/
│   │       ├── blog_list.html              # Шаблон страницы `blog_list` (список всех постов)
│   │       ├── blog_detail.html            # Шаблон страницы `blog_detail` (информация о посте)
│   │       ├── blog_form.html              # Шаблон страницы `blog_form` (форма добавления поста)
│   │       └── blog_confirm_delete.html    # Шаблон страницы `blog_confirm_delete` (удаление поста)
│   ├── models.py                   # Модель Блога
│   ├── views.py                    # Контроллеры Блога
│   ├── urls.py                     # Маршруты приложения 
│   ├── admin.py                    # Настройки админ-панели
│   ├── apps.py             
│   └── tests.py             
├── catalog/                                # Приложение каталога товаров
│   └── management/
│       ├───__init__.py
│       └───commands/
│           ├───__init__.py
│           ├───add_products.py     # Кастомная команда наполнения данными
│           └───del_products.py     # Кастомная команда удаления данных
│   ├── migrations/                 # Директория для файлов миграции
│   ├── templates/                  # Шаблоны
│   │    └── includes/              
│   │    │  ├── footer.html         # Шаблон `подвала`
│   │    │  └── inc_menu.html       # Шаблон основного меню
│   │    └── catalog/
│   │       ├── base.html              # Шаблон главной страницы `base` 
│   │       ├── product_list.html      # Шаблон страницы `product_list` (список всех товаров)
│   │       ├── product_detail.html    # Шаблон страницы `product_detail` (информация о товаре)
│   │       ├── product_form.html      # Шаблон страницы `product_form` (форма добавления товара)
│   │       ├── success_page.html      # Шаблон страницы `product_confirm_delete` (удаление товара)
│   │       └── contacts.html          # Шаблон страницы `contacts`
│   ├── templatetags/               # Кастомная логика в шаблонах (фильтр - `media_filter`) 
│   ├── models.py                   # Модели Категория и Продукт
│   ├── views.py                    # Контроллеры Продукта
│   ├── urls.py                     # Маршруты приложения 
│   ├── admin.py                    # Настройки админ-панели
│   ├── apps.py             
│   ├── forms.py                    # Настройки форм             
│   └── tests.py             
├── static/                         # CSS/JS/Изображения
├── media/                          # Директория для медиа-файлов
├── .flake8                 
├── .gitignore                 
├── LICENSE.txt                 
├── poetry.lock                
├── pyproject.toml                
├── README.md                
└── manage.py

## Модели приложения

Приложение содержит следующие основные модели:

1. `Category` (Категория товаров)
Поля:
- `name` - Наименование (CharField, max_length=100)
- `description` - Описание (TextField, опционально)

Особенности: Сортировка по названию.

Строковое представление: название категории.

2. `Product` (Товар)
Поля:
- `name` - Наименование (CharField, max_length=150)
- `description` - Описание (TextField, опционально)
- `image` - Изображение (ImageField)
- `category` - Связь с категорией (ForeignKey)
- `price` - Цена (DecimalField)
- `created_at`/`updated_at` - Даты создания и обновления

Особенности: Сортировка по названию и цене.

Строковое представление включает название, категорию и цену.

3. `Contact` (Контактные данные)
Поля:
- `address` - Адрес (CharField)
- `phone` - Телефон (CharField)
- `email` - Email (EmailField)

Строковое представление содержит все контактные данные.

4. `Blog` (Блог)
Поля:
- `title` - Заголовок поста (CharField)
- `author` - Автор поста (CharField)
- `content` - Описание (TextField)
- `preview` - Превью (ImageField)
- `created_at` - Дата создания (DateTimeField)
- `is_published` - Отметка о публикации (BooleanField)
- `counter` - Счетчик просмотров (PositiveIntegerField)

Строковое представление включает заголовок и дату создания поста.

Особенности: Сортировка по заголовкам, контенту, дате создания и количеству просмотров.


## Администрирование (админ-панель)

Приложение предоставляет следующие возможности в Django Admin:
1. Категории (`Category`):
- Отображаемые поля: ID, Название
- Фильтры: По названию
- Поиск: По названию и описанию
- Сортировка: По названию (по умолчанию)

2. Товары (`Product`):
- Отображаемые поля: ID, Название, Цена, Категория
- Фильтры: По категории и названию
- Поиск: По названию и описанию
- Сортировка: По названию и цене (по умолчанию)

3. Контакты (`Contact`):
- Отображаемые поля: Адрес, Телефон, Email
- Особенности: Все поля обязательные для заполнения

4. Блог (`Blog`):
- Отображаемые поля: id, Заголовок, Автор, Дата создания, Контент, Статус публикации.
- Сортировка: по заголовкам, авторам, датам создания и статусам публикации.
- Поиск: по заголовкам, авторам, контенту, датам создания и статусам публикации.

Как создать суперпользователя:

```
python manage.py createsuperuser
```
[Админ-панель](http://127.0.0.1:8000/admin/)


## Кастомные команды управления

Приложение включает следующие команды для работы с данными:

1. `del_products.py` - Deleting data from a database:
Назначение: Полная очистка каталога (удаление всех товаров и категорий).
Запуск:
```
python manage.py del_products
```
Действие:
- Удаляет все записи Product
- Удаляет все записи Category
- Выводит сообщение об успешном выполнении

Пример вывода:
```
Successfully deleted data from database
```

2. `add_products.py` - Add test products to the database and load test data from fixture:
Назначение: Наполнение базы тестовыми данными.
Запуск:
```
python manage.py add_products
```
Действие:
- Создает категорию "Пеларгонии" (если не существует)
- Добавляет 3 тестовых товара:
* Quantock Classic (1050 руб.)
* Patricia Andrea (970 руб.)
* Chocolate Peppermint (1100 руб.)
- Загружает дополнительные данные из catalog_fixture.json
- Для каждого товара выводит информацию:
* Успешное создание или
* Предупреждение, если товар уже существует

Пример вывода:
```
Successfully added product: Quantock Classic Пеларгонии/
Product already exists: Patricia Andrea Пеларгонии
Successfully loaded data from fixture
```

## Контроллеры (CBV)

### Приложение `blog`:

1. `class BlogListView(ListView)`:
Назначение: Главная страница со всеми постами.
1.1. `get_queryset()` - добавляет условие об отображении записей блога с отметкой 'is_published'

2. `class BlogDetailView(DetailView)`:
Назначение: Страница с детальной информацией о посте.
2.1. `get_object()` - Увеличивает количество просмотров поста при каждом его открытии.
2.2. `get_context_data()` - Дополняет контекст шаблона отображения поста.
Получает 5 последних постов (сортировка по дате создания).

3. `class BlogCreateView(CreateView)`:
Назначение: Страница для создания нового поста.

4. `class BlogUpdateView(UpdateView)`:
Назначение: Страница для редактирования поста.
4.1. `def get_success_url()` - Возвращает на страницу поста после его редактирования.

5. `class BlogDeleteView(DeleteView)`:
Назначение: Страница для удаления поста.


### Приложение `catalog`:

1. `class ProductListView(ListView)`:
Назначение: Главная страница со всеми товарами.

2. `class ProductDetailView(DetailView)`:
Назначение: Страница с детальной информацией о товаре.
2.1. `get_context_data()` - Дополняет контекст шаблона отображения товара.
Получает 5 последних добавленных товаров-новинок (сортировка по дате создания).

3. `class ProductCreateView(CreateView)`:
Назначение: Страница для создания нового товара.

4. `class ProductUpdateView(UpdateView)`:
Назначение: Страница для редактирования товара.
4.1. `def get_success_url()` - Возвращает на страницу товара после его редактирования.

5. `class ProductDeleteView(DeleteView)`:
Назначение: Страница для удаления товара.

## Контроллеры FBV:
1. `contacts()`:
Назначение: Страница контактов с формой обратной связи.
Методы: GET/POST.

- Логика GET:
Получает первый объект контактов из БД.
Рендерит шаблон `contacts.html` с контекстом:
python
`{"contact": Contact}`  # Контактные данные

- Логика POST:
Получает данные формы:
* `name` (обязательно)
* `phone` (опционально)
* `message` (опционально)
Возвращает текстовый ответ с благодарностью.
Пример POST-ответа:
"Спасибо, Иван! Ваше сообщение получено."


## Формы приложения `catalog` (`forms.py`):

1.`class StyleFormMixin()`:
Миксин для автоматической стилизации полей форм Django.

Функциональность:
- Автоматически добавляет CSS-классы к полям формы:
* BooleanField → form-check-input
* ChoiceField → form-select
* Все остальные поля → form-control

Использование: в пользовательских формах(`ProductForm`).

2. `class ProductForm(StyleFormMixin, forms.ModelForm)`:
Форма для создания и редактирования товаров.

Особенности:
- Валидация текстовых полей на наличие запрещенных слов (FORBIDDEN_WORDS)
- Проверка цены на отрицательные значения
- Валидация изображений:
* Поддерживаемые форматы: JPEG, JPG, PNG
* Максимальный размер: 5MB
* Автоматическая подстановка изображения по умолчанию при отсутствии загрузки

Методы валидации:
- `clean_name()` - проверка названия на запрещенные слова
- `clean_description()` - проверка описания
- `clean_price()` - проверка цены
- `clean_image()` - валидация изображения


## Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE.txt).