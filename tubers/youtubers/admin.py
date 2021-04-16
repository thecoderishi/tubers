from django.contrib import admin
from django.utils.html import format_html

from .models import Youtuber
# Register your models here.

class YtAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="50" />'.format(object.photo.url))
    list_display = ('id', 'myphoto', 'name', 'subs_count', 'price', 'camera_type', 'category', 'is_featured')
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'camera_type', 'category')
    list_editable = ('is_featured',)


admin.site.register(Youtuber,YtAdmin)