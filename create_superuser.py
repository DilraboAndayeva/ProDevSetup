import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.core.management import call_command

User = get_user_model()

# 1. Superuser yaratish (agar oldin yaratilmagan bo'lsa)
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin1234')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' muvaffaqiyatli yaratildi!")
else:
    print(f"Superuser '{username}' allaqachon mavjud.")

# 2. data.json faylidan maqolalarni bazaga yuklash
try:
    print("data.json dan ma'lumotlar yuklanmoqda...")
    call_command('loaddata', 'data.json')
    print("Maqolalar va kategoriyalar bazaga muvaffaqiyatli yuklandi!")
except Exception as e:
    print(f"Ma'lumotlarni yuklashda xatolik: {e}")