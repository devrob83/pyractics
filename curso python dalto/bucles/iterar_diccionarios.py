diccionario = {
    "nombre": "Robinson",
    "apellido": "Padilla",
    "altc": 140
}

#recorriendo diccionario para obtener la clave 
for key in diccionario:
    key 
    value = datos[1]
    print(f"la clave es:{key}")
    
#recorriendo diccionario con items() para obtener las claves y el valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es:{key} y el valor es: {value}")