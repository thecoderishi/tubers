from django.contrib import admin

from .models import ContactForm
# Register your models here.

class contactusAdmin(admin.ModelAdmin):

    list_display = ('id', 'full_name', 'company', 'email', 'subject')
    list_display_links = ('id', 'full_name',)

admin.site.register(ContactForm, contactusAdmin)
