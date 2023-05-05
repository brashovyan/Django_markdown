from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mainapp.views import *
from secondapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="index"),
    path('secondapp/', Index2.as_view(), name="index2"),
    path('markdownx/', include('markdownx.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)