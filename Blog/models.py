from django.db import models
from theBank import settings
from django.utils.safestring import mark_safe
from django.utils import timezone
from tinymce.models import HTMLField

# Create your models here.


class BlogCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category name')

    def __str__(self):
        return self.name

    def get_blogs(self):
        return self.blog_set.all()


class Blog(models.Model):
    name = models.TextField(verbose_name='Blog name')
    date_posted = models.DateTimeField(default=timezone.now, verbose_name='Date of posting')
    image = models.ImageField(upload_to='propetyMarket/images/Blog/main/', verbose_name='Blog image')
    content = HTMLField(verbose_name='Blog content')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name='Category name')
    description = models.TextField(verbose_name='Blog description')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='blog author')

    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.content = mark_safe(self.content)
        self.name = mark_safe(self.name)
        self.description = mark_safe(self.description)
        super(Blog, self).save()
