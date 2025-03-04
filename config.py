from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict

logger.configure()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
    BD_URL: str = "mysql+pymysql://root:@localhost/books"
    CORS_ORIGINS: list[str] = ["*"]
    SKIP_AUTH: bool = True


settings = Settings()
