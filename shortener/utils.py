import random
import string
from .models import URL

def generate_short_code(length=6):
    short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    while URL.objects.filter(short_code=short_code).exists():
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return short_code

