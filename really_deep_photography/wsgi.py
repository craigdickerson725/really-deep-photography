import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'really_deep_photography.settings')

application = get_wsgi_application()