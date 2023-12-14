from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls
from mysite import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', include('catalog.urls')),
    path('portfolio/', include('portfolio.urls')),
]

urlpatterns += doc_urls
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)