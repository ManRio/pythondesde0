from django.contrib import admin
from .models import Page

# Configuracion extra del panel de administración
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'visible', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    ordering = ('-created_at',)



# Register your models here.

admin.site.register(Page, PageAdmin)

# Configuración del panel de administración

title = "Proyecto con Django"
subtitle = "Panel de Gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
