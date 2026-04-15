# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:02:09 2026

@author: bausi
"""

def cargar_datos(ruta):
    
    '''
    Lee el archivo CSV y devuelve una lista de registros.
    
    Parametros:
        - ruta: ruta de el archivo.
        
    Retorna:
        - list: registros del sistema
        
    '''
    datos = []
    try:
        with open(ruta, "r") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                
                registro = {"id": int(partes[0]),
                            "fecha": partes[1],
                            "app": partes[2],
                            "valor1": int(partes[3]),
                            "vlaor2":int(partes[4]) }
                datos.append(registro)
                
    except Exception as e: 
        print("Error al cargar datos:", e)
        
    return datos