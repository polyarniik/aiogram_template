# Here you can declare bot settings in order to use them in the future.
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BOT_TOKEN = os.environ.get("BOT_TOKEN")
DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_SERVER = os.environ.get("DATABASE_SERVER")
