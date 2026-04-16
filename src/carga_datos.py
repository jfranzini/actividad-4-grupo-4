
def cargar_datos(ruta):
    
    '''
    Lee el archivo CSV y devuelve una lista de registros.
    
    Parametros:
        - ruta: ruta de el archivo.
        
    Retorna:
        - list: lista de diccionarios con los registros del sistema
        
    '''
    datos = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            
            registro = {
                "id_participante": int(partes[0]),
                "fecha": partes[1],
                "app": partes[2],
                "cantidad_uso": int(partes[3]),
                "tiempo_uso": int(partes[4])
            }
           
            datos.append(registro)
           
    return datos
