from django.contrib import admin
from .models import FaqCategory, Faq

# Register your models here.
admin.site.register(FaqCategory)
admin.site.register(Faq)