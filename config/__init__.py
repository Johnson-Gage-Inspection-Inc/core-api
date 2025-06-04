# config/__init__.py
from dotenv import load_dotenv

# Load safe defaults first
load_dotenv(dotenv_path="config/settings.env", override=False)

# Load secrets (overrides if duplicated)
load_dotenv(dotenv_path=".env", override=True)
