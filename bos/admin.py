from django.contrib import admin

from .models import BOS, BOS_topic, BOS_shift, BOS_area


#admin.site.register(BOS)
@admin.register(BOS)
class BOSadmin(admin.ModelAdmin):
    list_display = ['__str__', 'owner', 'Area']

admin.site.register(BOS_topic)
admin.site.register(BOS_shift)
admin.site.register(BOS_area)


admin.site.site_header = "JDE application Admin"
admin.site.site_title = "JDE App"
admin.site.index_title = "Welcome to JDE App Portal"