from django.contrib import admin

# Register your models here.
from .models import Fiction

class FictionAdmin(admin.ModelAdmin):
    search_fields = ['fiction_subject']

admin.site.register(Fiction, FictionAdmin)
