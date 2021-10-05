from django.core.cache import cache

from .models import *
from .forms import *

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.all()
            cache.set('cats', cats, 60)

        context['cats'] = cats
        return context
