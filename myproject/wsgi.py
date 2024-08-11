import os

from django.core.wgsi import get_wgsi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = get_wgsi_application()

app = application