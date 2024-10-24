import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'really_deep_photography.settings')

application = get_asgi_application()