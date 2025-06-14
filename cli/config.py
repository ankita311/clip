from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    api_base_url: str
    api_base_user: str
    api_base: str

    class Config:
        env_file = ".env"

settings = Settings()