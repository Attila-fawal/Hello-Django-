import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

# Load environment variables from .env file
project_folder = os.path.expanduser('~/django_todo')
load_dotenv(os.path.join(project_folder, '.env'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_todo.settings')
application = get_wsgi_application()
