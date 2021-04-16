
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webpages.urls')),
    path('youtubers/', include('youtubers.urls')),
    path('hiretubers/', include('hiretubers.urls')),
    path('accounts/', include('accounts.urls')),
    path('contactus/', include('contactus.urls')),
    path('socialaccounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
