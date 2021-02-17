from django.contrib import admin
from .models import Region

# Register your models here.
class RegionAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')
admin.site.register(Region, RegionAdmin)