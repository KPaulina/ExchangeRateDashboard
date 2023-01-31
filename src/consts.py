import os
import dotenv

dotenv.load_dotenv()

DB_NAME = os.environ.get('POSTGRES_DB')
DB_USER = os.environ.get('POSTGRES_USER')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DB_HOST = os.environ.get('POSTGRES_HOST')
DB_PORT = os.environ.get('POSTGRES_PORT')

RENDER_DATABASE = os.getenv("RENDER_DATABASE")
RENDER_USER = os.getenv("RENDER_USER")
RENDER_PASSWORD = os.getenv("RENDER_PASSWORD")
RENDER_PORT = os.getenv("RENDER_PORT")
RENDER_HOSTNAME = os.getenv("RENDER_HOSTNAME")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))[:-3]
DATA_DIR = os.path.join(BASE_DIR, 'data')
