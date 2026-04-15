# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:11:11 2026

@author: bausi
"""

from src.carga_datos import cargar_datos
from src.validacion_datos import filtrar_registros_validos
from src.procesamiento_datos import preparar_datos
from src.metricas import calcular_metricas

def main():
    ruta = "datos/BehaviorTracker_mock_data.csv"
    
    try:
        datos = cargar_datos(ruta)
        datos_validos = filtrar_registros_validos(datos)
        datos_procesados = preparar_datos(datos_validos)
        resultados = calcular_metricas(datos_procesados)
        
        print("Resultados:", resultados)
        
    except Exception as error: 
        print("Error critico en main: ", error)
        
main()
