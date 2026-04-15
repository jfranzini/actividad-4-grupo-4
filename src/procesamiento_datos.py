# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:06:37 2026

@author: bausi
"""

def preparar_datos(datos):  
    '''
    Prepara los datos para el analisis.
    Parametros: 
        - datos: lista de registros validos.
    Retorna:
        - list: datos procesados.
    '''
    datos_procesados = []
    for registro in datos:
        nuevo_registro = {
            "id_participante": registro["id_participante"],
            "fecha": registro["fecha"],
            "app": registro["app"].strip().lower(),
            "cantidad_uso": registro["cantidad_uso"],
            "tiempo_uso": registro["tiempo_uso"]}

        datos_procesados.append(nuevo_registro)

    return datos_procesados
