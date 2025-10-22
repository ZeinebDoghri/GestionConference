from django.contrib import admin
from .models import User, organizingCommittee
# Register your models here.
#admin.site.register(User)
#admin.site.register(organizingCommittee)

class OrginizingCommitteeInline(admin.TabularInline):
    model = organizingCommittee # Model to be displayed inline
    extra = 1 # Number of extra forms to display
    readonly_fields = ('date_joined',) # Make fields read-only
    fieldsets = (
        ("Committee Information", {
            'fields': ('user', 'conference', 'committee_role', 'date_joined')
        }),
    )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'first_name', 'last_name', 'affiliation', 'email', 'role', 'nationality', 'last_login', 'date_joined') # Add columns to the list view
    ordering = ('-date_joined',) # Order by date_joined descending
    search_fields = ('username', 'first_name', 'last_name', 'email', 'affiliation') # Add a search bar to filter by username, first name, last name, email, and affiliation
    list_filter = ('role', 'date_joined') # Add a filter sidebar to filter by role and date_joined
    fieldsets = (
        ("Personal Information", {
            'fields': ('user_id', 'username', 'first_name', 'last_name', 'email', 'affiliation', 'nationality')
        }), 
        ("Permissions", {
            'fields': ('role', 'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions') # Django built-in fields for permissions
        }),
        ("Important Dates", {
            'fields': ('last_login', 'date_joined')# Django built-in fields for important dates 
        })
    )
    readonly_fields = ('user_id', 'last_login', 'date_joined') # Make user_id, last_login, and date_joined read-only
    inlines = [OrginizingCommitteeInline] # Add the inline to the User admin page
    

@admin.register(organizingCommittee)
class OrganizingCommitteeAdmin(admin.ModelAdmin):    
    list_display = ('user', 'conference', 'committee_role', 'date_joined') # Add columns to the list view
    ordering = ('conference',) # Order by conference ascending
    search_fields = ('user', 'conference', 'committee_role') # Add a search bar to filter by user, conference, and committee_role
    list_filter = ('committee_role', 'conference') # Add a filter sidebar to filter by committee_role and conference
    fieldsets = (
        ("Committee Information", {
            'fields': ('user', 'conference', 'committee_role', 'date_joined')
        }),
    )

