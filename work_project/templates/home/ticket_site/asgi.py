"""
<<<<<<<< HEAD:work_project/ticket_site/asgi.py
ASGI config for ticket_site project.
========
ASGI config for work_project project.
>>>>>>>> 9275fdb (change name project):work_project/work_project/asgi.py

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<<< HEAD:work_project/ticket_site/asgi.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticket_site.settings')
========
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'work_project.settings')
>>>>>>>> 9275fdb (change name project):work_project/work_project/asgi.py

application = get_asgi_application()
