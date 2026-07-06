import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database
DATABASE_URL = os.getenv("DATABASE_URL")

# Redis
REDIS_URL = os.getenv("REDIS_URL")

# Authentication
SECRET_KEY = os.getenv("SECRET_KEY")

MONGO_URL = os.getenv("MONGO_URL")
