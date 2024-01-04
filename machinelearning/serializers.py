from rest_framework import serializers

from .models import Diagnostico

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = ('id','enfermedad','procentaje','ficha','fecha_analisis')
        read_only_fields = ('fecha_analisis',)