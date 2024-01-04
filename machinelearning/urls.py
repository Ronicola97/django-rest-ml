from rest_framework import routers
from .api import DiagnosticoViewSet

router = routers.DefaultRouter()

router.register('api/diagnostico',DiagnosticoViewSet,'diagnostico')

urlpatterns = router.urls