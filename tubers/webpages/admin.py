from django.contrib import admin

from django.utils.html import format_html

from .models import Slider, Team

# Register your models here.

class teamAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="50" />'.format(object.photo.url))

    list_display = ('id', 'myphoto', 'first_name', 'role')
    list_display_links = ('id', 'first_name',)
    search_fields = ('first_name', 'last_name')

class sliderAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html('<img src="{}" width="50" />'.format(object.photo.url))
    list_display = ('id', 'headline', 'myphoto', 'button_text')
    list_display_links = ('id', 'headline')

admin.site.register(Slider, sliderAdmin)
admin.site.register(Team, teamAdmin)