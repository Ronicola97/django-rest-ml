from machinelearning.models import Diagnostico
from rest_framework import viewsets, permissions
from .serializers import DiagnosticoSerializer

class DiagnosticoViewSet(viewsets.ModelViewSet):
    queryset = Diagnostico.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DiagnosticoSerializer