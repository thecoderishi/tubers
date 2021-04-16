from django.contrib import admin
from .models import Hiretuber
# Register your models here.


class HireTuberAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'phone', 'tuber_name',)
    list_display_link = ('id', 'first_name',)
    search_fields = ('tuber_name',)



admin.site.register(Hiretuber,HireTuberAdmin)
