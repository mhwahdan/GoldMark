from django.contrib import admin
from flat_json_widget.widgets import FlatJsonWidget
from django.db import models
from .models import Property, Location, Bank, Developer, Agent, PropertyImage


# Register your models here.
class PropertyDetailsInline(admin.TabularInline):
    model = PropertyImage


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyDetailsInline]
    formfield_overrides = {
        models.JSONField: {'widget': FlatJsonWidget},
    }

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(agent=request.user)


admin.site.register(Property, PropertyAdmin)
admin.site.register(Location)
admin.site.register(Bank)
admin.site.register(Developer)
admin.site.register(Agent)
