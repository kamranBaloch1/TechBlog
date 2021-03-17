
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "TechWorld Admin"

admin.site.site_title = "TechWorld "


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('TechWorld.urls'))
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
