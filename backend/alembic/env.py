"""Alembic environment configuration"""

import sys
from pathlib import Path

# プロジェクトルート（app パッケージを含むディレクトリ）を Python パスに追加
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from logging.config import fileConfig  # noqa: E402

from sqlalchemy import engine_from_config, pool  # noqa: E402

from alembic import context  # noqa: E402
from app.database import Base  # noqa: E402
from app.models import Item  # noqa: E402, F401  — モデルを読み込んでメタデータに登録

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
