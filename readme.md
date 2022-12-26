# Сервис сбора пожертвований

![Cats](_assets/main.png)

## Для чего

Сервис сбора пожертвований на различные целевые проекты для поддержки котиков.

Проекты:

- У каждого проекта есть название, описание и сумма, которую планируется собрать.
- После того, как нужная сумма собрана — проект закрывается.

Пожертвования:

- Пользователь может сделать пожертвование и дополнить его комментарием.
- Пожертвования вносятся в фонд, а не в конкретный проект.
- Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму.
- Если пожертвование больше нужной суммы или же в фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта.
- При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

Пользователи:

- Не зарегистрированный пользователь может видеть список всех проектов для пожертвований.
- Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.
- Проекты для пожертвований создаются администраторами (суперпользователями).

Документация и примеры запросов API доступны в Swagger и ReDoc, по адресу (http://127.0.0.1:8000/docs и http://127.0.0.1:8000/redoc)

## Используемые технологии

В проекте были применены:

- FastApi = асинхронный веб-фреймворк для создания API
- FastAPI Users = библиотека для регистрации и аутентификации пользователей в FastApi
- SQLAlchemy = ORM для работы с РСУБД
- Alembic = для миграций БД
- Pydantic = валидация данных с использованией тайп-хитингов
- Aiosqlite = асинхронный интерфейс для SQLite
- Uvicorn = ASGI веб-сервер
- Swagger = для документирования Api и его ручек

Дополнительно:

- При работе с проектом была применена методика `Conventional Commits` ([подробнее по ссылке](https://www.conventionalcommits.org/en/v1.0.0/))
- Настроены `Pre-commit Hooks` ([подробнее по ссылке](https://pre-commit.com/))
- Первоначальная (базовая) настройка `Docker`

## Подготовка к запуску

Клонируйте проект из репозитория:

```bash
git clone https://github.com/budaevdigital/QRCats.git
```

И перейдите в директорию проекта:

```bash
cd QRCats/
```

В корневой директории проекта создайте файл `.env` и пропишите там настройки для отображаемого названия приложения и драйвер БД с директорией к файлу БД:

```text
APP_TITLE=Сервис бронирования переговорных комнат
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET_KEY=SECRET
FIRST_SUPERUSER_EMAIL=example@email.com
FIRST_SUPERUSER_PASSWORD=1234567890
```

Пароль для `SECRET_KEY` можно сгенерировать и скопировать в терминале, с помощью команды:

```bash
openssl rand -hex 32
```

> `SECRET_KEY` нужен для генерации токенов для пользователей

> `FIRST_SUPERUSER_EMAIL` и `FIRST_SUPERUSER_PASSWORD` - нужны для создания Администратора, который будет создан автоматически при первом запуске проекта

Создайте и активируйте виртуальное окружение командой:

```python
python -m venv venv
source venv/bin/activate
```

И выполните установку всех зависимостей проекта:

```python
pip install -r requirements.txt
```

Когда установка зависимостей завершиться, можно запускать проект, но перед этим необходимо произвести миграции в БД:

```bash
alembic upgrade head
```

## Работа с проектом

Запускаем проект:

```bash
uvicorn app.main:app --reload
```

Переходим по адресу http://127.0.0.1:8000/docs - откроется интерфейс Swagger в котором вы сможете ознакомиться с эндпоинтами и типами запросов.

## Запуск с помощью Docker

Клонируйте репозиторий, подготовьте `.env` файл, как это указано выше, перейдите в директорию и помощью команды выполните сборку образа:

```bash
docker image build -t qrkats .
```

> сам Docker у вас должен быть уже запущен

Запустите образ:

```bash
docker run -p 80:80 qrkats
```

Переходим по адресу http://0.0.0.0/docs - откроется интерфейс Swagger в котором вы сможете ознакомиться с эндпоинтами и типами запросов.

Для удаления этого образа, просто введите команду:

```bash
docker rmi qrkats --force
```

---

Автор проекта: Дмитрий Будаев
