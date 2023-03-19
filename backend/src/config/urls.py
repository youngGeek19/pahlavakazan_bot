from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from menu.views import ProductViewSet, OrderViewSet, ClientViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'product', ProductViewSet)
router.register(r'order', OrderViewSet)
router.register(r'client', ClientViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)