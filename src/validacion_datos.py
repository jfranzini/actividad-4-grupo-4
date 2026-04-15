# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:04:50 2026

@author: bausi
"""

def validar_registro(registro):
    '''
    Valida el registro de Behaviour Tracker.

    Parametros:
        - registro : diccionario con un registro.
        
    Retorna :
        - dict: regsitro validado con tipos corregidos.

    '''
    try: 
        id_participante = int(registro["id_participante"])
        fecha = registro ["fecha"].strip()
        app = registro["app"].strip()
        cantidad_uso = int(registro["cantidad_uso"])
        tiempo_uso = int(registro["tiempo_uso"])
        
        if fecha == "":
            raise ValueError("La fecha esta vacia")
            
        if app == "":
            raise ValueError("La app esta vacia")
            
        if cantidad_uso < 0:
            raise ValueError("cantidad_uso no puede ser negativa")
            
        if tiempo_uso < 0:
            raise ValueError("tiempo_uso no puede ser negativo")
            
        return {"id_participante": id_participante, "fecha": fecha, "app": app, "cantidad_uso": cantidad_uso, "tiempo_uso": tiempo_uso}
    
    except KeyError as error:
        raise KeyError("falta el campo", error)
        
    except ValueError as error:
        raise ValueError("error de validacion", error)
    
    
def filtrar_registros_validos(datos):
    
    '''
    Valida los regsitros del sistema.
    
    Parametros:
        - datos: lista de registros.
        
    Retorna:
        - list: registros validos.
        
    '''
    datos_validos = []
    numero_registro = 1
    
    for registro in datos:
        try:
            registro_valido = validar_registro(registro)
            datos_validos.append(registro_valido)
        
        except Exception as error:
           print("Error en registro", numero_registro, ":", error)
            
        numero_registro += 1
    
    return datos_validos
