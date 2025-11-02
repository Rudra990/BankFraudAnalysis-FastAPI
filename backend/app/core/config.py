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


print("Loaded PROJECT_NAME:", Settings().PROJECT_NAME)
settings = Settings()
