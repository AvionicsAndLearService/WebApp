from django.contrib import admin
from .models import ot, calificacion
# Register your models here.

class otadmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    
admin.site.register(ot, otadmin)

admin.site.register(calificacion)
