from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from alembic.config import Config
from alembic import command

# Настройки соединения с базой данных
DATABASE_URL = 'postgresql://Susan:www4556www@localhost/my_custom_db'

# Создание движка
engine = create_engine(DATABASE_URL)

# Если база данных не существует, создаем ее
if not database_exists(engine.url):
    create_database(engine.url)
    print("Database created successfully.")

# Конфигурация Alembic
alembic_cfg = Config("alembic.ini")

# Выполнение миграции до последней версии
command.upgrade(alembic_cfg, "head")
print("Migration applied successfully.")

