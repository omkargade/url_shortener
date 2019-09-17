import random, string
from .models import Shorted


def url_generator(size=6, chars=string.ascii_lowercase + string.ascii_uppercase+ string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_short():
    new_short = url_generator()
    while Shorted.objects.filter(short_url=new_short).exists():
        new_short = url_generator()
    return new_short
