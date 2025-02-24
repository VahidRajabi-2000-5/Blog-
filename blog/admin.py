from django.contrib import admin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "datetime_created",
        "datetime_modified",
        "status",
    ]
    
    list_editable = ['status']
