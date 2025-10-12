from django.contrib import admin
from .models import Conference, Submission
# Register your models here.
admin.site.site_header = "Conference Management Admin 25/26"
admin.site.site_title = "Conference Management Admin Portal"
admin.site.index_title = "Welcome to Conference Management Admin Portal"
#admin.site.register(Conference) Register the Conference model to make it accessible in the admin interface
admin.site.register(Submission)

# Tabular inline
class SubmissionInline(admin.TabularInline):
    model = Submission # Model to be displayed inline
    extra = 1 # Number of extra forms to display
    readonly_fields = ('submission_id',) # Make fields read-only
    fieldsets = (
        ("General Information", {
            'fields': ('submission_id', 'user', 'title', 'status')
        }),
    )

@admin.register(Conference) #Decorator to register the model
class AdminPersonalized(admin.ModelAdmin):
    list_display = ('name', 'theme', 'location', 'start_date', 'end_date', 'duration') #Add columns to the list view
    ordering = ('-start_date',) #Order by start_date descending
    search_fields = ('name', 'theme', 'location') #Add a search bar to filter by name, theme, and location
    list_filter = ('theme', 'location') #Add a filter sidebar to filter by theme and location
    fieldsets = (
        ("General Information", {
            'fields': ('conference_id', 'name', 'description', 'theme')
        }),

        ("Logistics", {
            'fields': ('start_date', 'end_date', 'location')
        })
    )
    readonly_fields = ('conference_id',) #Make conference_id read-only
    date_hierarchy = 'start_date' #Add a date-based drilldown navigation by start_date
    inlines = [SubmissionInline] #Add the inline to the Conference admin page
    def duration(self, obj): #obj is the instance of the model 
        if obj.start_date and obj.end_date: #Check if both dates are not None
            return (obj.end_date - obj.start_date).days
        return "RAS"
    duration.short_description = 'Duration (days)' #Change the column header name
    
