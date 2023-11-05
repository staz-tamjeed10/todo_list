from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'created_at', 'completed')
    list_filter = ('completed',)
    search_fields = ('task_name', 'created_at')

# Register the Task model for the admin site
# admin.site.register(Task, TaskAdmin)
