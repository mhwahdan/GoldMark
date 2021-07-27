from django.contrib import admin
from flat_json_widget.widgets import FlatJsonWidget
from django.db import models
from .models import Property, Location, Bank, Developer, Agent, PropertyImage, \
                    FaqCategory, Faq, BlogCategory, Blog
from tinymce.widgets import TinyMCE
from django import forms


# Register your models here.
class PropertyDetailsInline(admin.TabularInline):
    model = PropertyImage


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyDetailsInline]
    formfield_overrides = {
        models.JSONField: {'widget': FlatJsonWidget},
    }


class StopAdminForm(forms.ModelForm):
    class Meta:
        model = Blog
        widgets = {
          'content': TinyMCE(),
        }
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    form = StopAdminForm


admin.site.register(Property, PropertyAdmin)
admin.site.register(Location)
admin.site.register(Bank)
admin.site.register(Developer)
admin.site.register(Agent)
admin.site.register(FaqCategory)
admin.site.register(Faq)
admin.site.register(BlogCategory)
admin.site.register(Blog, BlogAdmin)
