from django.contrib import admin

from collection.models import Service

class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Service, ServiceAdmin)
