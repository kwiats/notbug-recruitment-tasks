from django.contrib import admin
from blog.models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
    ]

    fields = [
        "title",
        "entries",
        "author",
    ]
