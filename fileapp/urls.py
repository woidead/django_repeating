from django.contrib import admin, auth
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from fileapp.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('news/', include("news.urls")),
    path('users', include('users.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)