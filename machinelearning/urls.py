from rest_framework import routers
from .api import DiagnosticoViewSet

from . import views
from django.urls import path

router = routers.DefaultRouter()

router.register('api/diagnostico',DiagnosticoViewSet,'diagnostico')

urlpatterns = router.urls+[
    path('run-python-script/', views.RunPythonScriptView.as_view(), name='run-python-script'),
]