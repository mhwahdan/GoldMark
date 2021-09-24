from django.contrib import admin
from Blog.models import Blog, BlogCategory

# Register your models here.


admin.site.register(BlogCategory)
admin.site.register(Blog)
