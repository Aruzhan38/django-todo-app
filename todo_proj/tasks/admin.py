from django.contrib import admin

from django.contrib import admin
from .models import Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','owner','is_completed','created_at')
    list_filter = ('is_completed',)
