import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Bu yerga o'zingiz xohlagan login, email va parolingizni yozing:
USERNAME = 'DilraboAndayeva'
EMAIL = 'admin@example.com'
PASSWORD = 'SizningParolingiz123'  # <-- Shu yerga o'z parolingizni yozing

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(username=USERNAME, email=EMAIL, password=PASSWORD)
    print("Superuser muvaffaqiyatli yaratildi!")
else:
    print("Superuser allaqachon mavjud.")
os.system('python manage.py loaddata data.json')