from django.contrib import admin
from .models import Article, Category

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ("create_at", "updated_at") #mostrar campos de solo lectura
    list_display = ("title", "public", "create_at")
    list_filter = ("public", "create_at")
    search_fields = ("title", "content")
    ordering = ("-create_at",)

# Configurar titulo del panel

title = "Aprendiendo Django - Administración"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = "Panel de Gestión"

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)