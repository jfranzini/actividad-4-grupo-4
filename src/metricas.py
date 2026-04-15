# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:08:08 2026

@author: bausi
"""

def calcular_metricas(datos):
    
    '''
    Calcula metricas del sistema.
    Parametros:
        - datos: lista de datos procesados.   
    Retorna:
        -dict: resultados.  
    '''

    total_tiempo = 0
    total_uso = 0
    cantidad_registros = len(datos)

    for registro in datos:
        total_tiempo += registro["tiempo_uso"]
        total_uso += registro["cantidad_uso"]

    promedio_tiempo = total_tiempo / cantidad_registros
    promedio_uso = total_uso / cantidad_registros

    return {"promedio_tiempo_uso": promedio_tiempo, "promedio_cantidad_uso": promedio_uso}
