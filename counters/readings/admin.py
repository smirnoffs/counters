from django.contrib import admin
from .models import Counter, Reading

admin.site.register(Counter)
admin.site.register(Reading)