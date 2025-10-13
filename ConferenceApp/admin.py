from django.contrib import admin
from .models import Conference, Submission
# Register your models here.
admin.site.site_header = "Conference Management Admin 25/26"
admin.site.site_title = "Conference Management Admin Portal"
admin.site.index_title = "Welcome to Conference Management Admin Portal"
#admin.site.register(Conference) Register the Conference model to make it accessible in the admin interface
#admin.site.register(Submission)

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

#Tabular Stacked inline
#class SubmissionInline(admin.StackedInline):
#    model = Submission # Model to be displayed inline
#    extra = 1 # Number of extra forms to display
#    readonly_fields = ('submission_id', 'submission_date') # Make fields read-only
#    fieldsets = (
#        ("General Information", {
#            'fields': ('submission_id', 'user', 'title', 'abstract', 'status', 'payed')
#        }),
#    )




@admin.register(Conference) #Decorator to register the model
class AdminPersonalized(admin.ModelAdmin):
    list_display = ('name', 'theme', 'location', 'start_date', 'end_date', 'duration') #Add columns to the list view
    ordering = ('-start_date',) #Order by start_date descending
    search_fields = ('name', 'description', 'location') #Add a search bar to filter by name, theme, and location
    list_filter = ('theme', 'location', 'start_date') #Add a filter sidebar to filter by theme and location
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

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('submission_id', 'title', 'user', 'conference', 'status', 'submission_date', 'payed', 'short_abstract') #Add columns to the list view
    #Ajouter une méthode personnalisée short_abstract qui tronque l’abstract à 50 caractères pour l’affichage rapide.
    def short_abstract(self, obj):
        if obj.abstract:
            return obj.abstract[:50] + '...' if len(obj.abstract) > 50 else obj.abstract
        return ''
    short_abstract.short_description = 'Abstract(short)'
    list_editable = ('status', 'payed') #Make status and payed editable in the list view
    ordering = ('-submission_date',) #Order by submission_date descending
    search_fields = ('title', 'user__username', 'keywords') #Add a search bar to filter by title, user, and conference
    list_filter = ('status', 'payed', 'submission_date','conference') #Add a filter sidebar to filter by status and payed
    fieldsets = (
        ("General Information", {
            'fields': ('submission_id', 'title', 'abstract', 'keywords')
        }),
        ("File and Conference", {
            'fields': ('paper', 'conference')
        }),
        ("Follow-up", {
            'fields': ('status', 'payed', 'user', 'submission_date')
        })
    )
    readonly_fields = ('submission_id', 'submission_date') #Make submission_id and submission_date read-only
    date_hierarchy = 'submission_date' #Add a date-based drilldown navigation by submission_date
    
