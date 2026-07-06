import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:123@localhost:5433/managmentdb")

# Redis
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

# Authentication
SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key-in-production")
