#crando diccionarios con dict()
diccionario = dict(nombre="Robinson", apellido="Padilla")

#las listas no pueden ser claves y usamos la funcion frozenset para meter conjuntos
diccionario = {frozenset(["Padilla","come"]):"mucho"}

#crerando diccionarios con fromkeys() valor por defecto: none
diccionario =dict.fromkeys(["nombre", "apellido"])

#crerando diccionarios con fromkeys() cmbindo el valor por defecto a "no se "
diccionario =dict.fromkeys(["nombre", "apellido"], "no se")

print(diccionario)
