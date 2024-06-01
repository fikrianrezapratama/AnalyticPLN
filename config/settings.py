import os
from dotenv import load_dotenv
import logging

# Load .env file
load_dotenv()

class Config:
    API_HOST = os.getenv('API_HOST')
    EMAIL = os.getenv('EMAIL')
    PASSWORD = os.getenv('PASSWORD')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')

def setup_logging():
    logging.basicConfig(level=Config.LOG_LEVEL,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')