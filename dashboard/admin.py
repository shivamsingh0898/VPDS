from django.contrib import admin

# Register your models here.
from dashboard.models import *

admin.site.site_header = "VPDS ADMIN"
admin.site.site_title = "VPDS ADMIN"


class VpmUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'specialization', 'avatar')
    list_filter = ('user',)
    search_fields = ('specialization',)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'project_completed', 'company_feedback', 'client_feedback', 'overall_rating')
    list_filter = ('user', 'overall_rating')
    search_fields = ('overall_rating',)


class LiveProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'field', 'StartDate', 'platform', 'team_id')
    list_filter = ('name', 'StartDate')
    search_fields = ('platform',)


class ProjectArchiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'field', 'platform', 'startDate', 'team_id', 'duration')
    list_filter = ('name', 'startDate', 'duration')
    search_fields = ('name',)


class UpcomingProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'field', 'platform', 'start_date')
    list_filter = ('name', 'platform', 'start_date')
    search_fields = ('platform',)


class ProjectsOnHoldAdmin(admin.ModelAdmin):
    list_display = ('name', 'field', 'platform', 'duration')
    list_filter = ('name', 'duration')
    search_fields = ('platform',)


class ProjectTeamAdmin(admin.ModelAdmin):
    list_display = ('manager_Name', 'member_one_Name', 'member_two_Name', 'member_three_Name', 'member_four_Name',)
    list_filter = ('manager_Name',)
    search_fields = ('manager_Name', 'manager_id')


admin.site.register(VpmUser, VpmUserAdmin)
admin.site.register(LiveProject, LiveProjectAdmin)
admin.site.register(ProjectTeam, ProjectTeamAdmin)
admin.site.register(ProjectArchive, ProjectArchiveAdmin)
admin.site.register(UpcomingProject, UpcomingProjectAdmin)
admin.site.register(ProjectsOnHold, ProjectsOnHoldAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(About)
admin.site.register(Contact)
