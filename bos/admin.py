from django.contrib import admin
from django.contrib.auth.models import Permission
from import_export.admin import ImportExportModelAdmin
from .models import BOS, Topic, Shift, Area
from permit_to_work.models import permit_to_work
admin.site.register(Permission)

#admin.site.register(BOS)
@admin.register(BOS)
class BOSadmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['__str__', 'owner', 'Area']

admin.site.register(permit_to_work)
admin.site.register(Topic)
admin.site.register(Shift)
admin.site.register(Area)


admin.site.site_header = "JDE application Admin"
admin.site.site_title = "JDE App"
admin.site.index_title = "Welcome to JDE App Portal"