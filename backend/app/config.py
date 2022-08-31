from pydantic import BaseSettings


class Settings(BaseSettings):
    postgres_url: str = 'postgresql://constricon_user:OwOtBep9Frut@db:5432/constricon'

    class Config:
        env_file = '.env'


settings = Settings()
