#keys() devuelve las claves, tambien funciona para iterar

#get() devuelve el valor de una clave

#clear() elimina todos los elementos

#pop() elimina un elemento

#items()para iterar el dict

diccionario = {
    "nombre" : 'Robinson',
    "apellido" : 'Padilla',
    "edad" : 40
}
#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get()  (si no encuentra nada el programa continua)
valor_de_papa = diccionario.get("papa")
print("el programa continua")


#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("edad")
#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)