from django.shortcuts import render
from .DecisionTreeClassifier import run

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


class RunPythonScriptView(APIView):

    def post(self, request):

        datos = request.data


        edad = int(datos.get("edad"))
        alo_cabe = int(datos.get("alo_cabe"))
        alo_ore = int(datos.get("alo_ore"))
        alo_cue = int(datos.get("alo_cue"))
        alo_lom = int(datos.get("alo_lom"))
        alo_ext = int(datos.get("alo_ext"))
        alo_abdo = int(datos.get("alo_abdo"))
        pica_lev = int(datos.get("pica_lev"))
        pica_mod = int(datos.get("pica_mod"))
        pica_int = int(datos.get("pica_int"))
        enrojecimiento = int(datos.get("enrojecimiento"))
        cost_peq = int(datos.get("cost_peq"))
        cost_med = int(datos.get("cost_med"))
        cost_gran = int(datos.get("cost_gran"))
        pg_lv = int(datos.get("pg_lv"))
        pg_pron = int(datos.get("pg_pron"))
        pg_gra = int(datos.get("pg_gra"))
        pust_peq = int(datos.get("pust_peq"))
        pust_gran = int(datos.get("pust_gran"))
        mal_olor = int(datos.get("mal_olor"))
        eritema = int(datos.get("eritema"))
        sacu_cabe = int(datos.get("sacu_cabe"))
        cerum_oid = int(datos.get("cerum_oid"))

        datos = [[edad,
        alo_cabe,
        alo_ore,
        alo_cue,
        alo_lom,
        alo_ext,
        alo_abdo,
        pica_lev,
        pica_mod,
        pica_int,
        enrojecimiento,
        cost_peq,
        cost_med,
        cost_gran,
        pg_lv,
        pg_pron,
        pg_gra,
        pust_peq,
        pust_gran,
        mal_olor,
        eritema,
        sacu_cabe,
        cerum_oid]]
        # Ejecutamos el script de Python
        result = run(datos)

        # Devolvemos el resultado del script de Python al cliente
        return Response(result)
    
    