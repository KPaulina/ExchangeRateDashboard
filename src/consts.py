import os
import dotenv

dotenv.load_dotenv()

DB_NAME = os.environ.get('POSTGRES_DB')
DB_USER = os.environ.get('POSTGRES_USER')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DB_HOST = os.environ.get('POSTGRES_HOST')
DB_PORT = os.environ.get('POSTGRES_PORT')

RENDER_DATABASE = os.environ.get("RENDER_DATABASE")
RENDER_USER = os.environ.get("RENDER_USER")
RENDER_PASSWORD = os.environ.get("RENDER_PASSWORD")
RENDER_PORT = os.environ.get("RENDER_PORT")
RENDER_HOSTNAME = os.environ.get("RENDER_HOSTNAME")
