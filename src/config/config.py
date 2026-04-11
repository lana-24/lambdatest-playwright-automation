import os
from dotenv import load_dotenv

load_dotenv()

UI_BASE_URL = os.getenv("UI_BASE_URL")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
