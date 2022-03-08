from django.contrib import admin
from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()
router.register('enderecos', EnderecoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
]
