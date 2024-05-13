import motor.motor_asyncio
from dotenv import load_dotenv
import os

load_dotenv()


DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_COLLECTION = os.environ.get('DB_COLLECTION')

client = motor.motor_asyncio.AsyncIOMotorClient(DB_HOST, int(DB_PORT))
db = client[DB_COLLECTION]
