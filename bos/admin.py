from django.contrib import admin

from .models import BOS, BOS_topic, BOS_shift, BOS_area
admin.site.register(BOS)
admin.site.register(BOS_topic)
admin.site.register(BOS_shift)
admin.site.register(BOS_area)