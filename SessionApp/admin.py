from django.contrib import admin
from .models import Session
# Register your models here.
#admin.site.register(Session)

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'session_day', 'start_time', 'end_time', 'room', 'conference') # Add columns to the list view
    ordering = ('-start_time',) # Order by start_time descending
    search_fields = ('title', 'topic', 'conference') # Add a search bar to filter by title, speaker, and description
    list_filter = ('topic', 'conference', 'session_day') # Add a filter sidebar to filter by conference and start_time
    fieldsets = (
        ("General Information", {
            'fields': ('title', 'topic', 'room', 'conference')
        }),
        ("Schedule", {
            'fields': ('session_day', 'start_time', 'end_time')
        })
    )
