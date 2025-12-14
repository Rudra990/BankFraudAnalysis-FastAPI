from pydantic_settings import BaseSettings, SettingsConfigDict 

from typing import Literal 
from pathlib import Path  

CURRENT_FILE = Path(__file__).resolve()
ENV_FILE = (CURRENT_FILE.parent.parent.parent.parent / ".envs" / ".env.local").resolve()

print("Resolved .env path using '..':", ENV_FILE, "Exists?", ENV_FILE.exists())

class Settings(BaseSettings):
  ENVIRONMENT: Literal["local","staging","production"] = "local"
  model_config = SettingsConfigDict(
    # env_file = "../../.envs/.env.local",env_ignore_empty=True,
    
    env_file = ENV_FILE,
    extra="ignore"
  )
  API_V1_STR: str = ""
  PROJECT_NAME: str = ""
  PROJECT_DESCRIPTION: str = ""
  SITE_NAME: str = ""
  DATABASE_URL: str = ""
  MAIL_FROM: str = ""
  MAIL_FROM_NAME: str = ""
  SMTP_HOST: str = "mailpit"
  SMTP_PORT: int = 1025
  MAILPIT_UI_PORT: int = 8025 

  REDIS_HOST: str = "redis"
  REDIS_PORT: int = 6379
  REDIS_DB:  int = 0

  RABBITMQ_HOST: str = "rabbitmq"
  RABBITMQ_PORT: int = 5672
  RABBITMQ_USER: str = "guest"
  RABBITMQ_PASSWORD: str = "guest"


print("Loaded PROJECT_NAME:", Settings().PROJECT_NAME)
settings = Settings()
