from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = "CandyDeliveryAppAPI"
    app_description: str = "API for candy delivery app"

    server_host: str = "127.0.0.1"
    server_port: int = 8000

    database_url: str


settings = Settings(
    _env_file=".env",
    _env_file_encoding="utf-8"
)
