import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = bool(os.getenv("FLASK_DEBUG", False))
    ENV = str(os.getenv("FLASK_ENV", "production"))
