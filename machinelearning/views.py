from django.shortcuts import render
from .DecisionTreeClassifier import run

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response 

class RunPythonScriptView(APIView):

    def post(self, request):
        # Obtenemos los parámetros del script de Python
        #name = request.data['name']
        name = "ronaldo"

        # Ejecutamos el script de Python
        result = run(name)

        # Devolvemos el resultado del script de Python al cliente
        return Response(result)
    
    