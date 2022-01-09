import os
from celery import Celery

# Создаем объект(экземпляр класса) celery и даем ему имя
# оно будет указываться при запуске celery в терминале:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'McDonalds.settings')

app = Celery('McDonalds')


# Загружаем config с настройками для объекта celery.
# т.е. импортируем настройки из django файла settings
# namespace='CELERY' - в данном случае говорит о том, что применятся будут только
# те настройки из файла settings.py которые начинаются с ключевого слова CELERY
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()