from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    RapidAPI_key: SecretStr

    class Config:
        env_file = 'settings.env'
        env_file_encoding = 'utf-8'


config = Settings()
