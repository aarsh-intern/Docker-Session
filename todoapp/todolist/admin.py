from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'description','created_at', 'updated_at')

admin.site.register(Todo, TodoAdmin)
