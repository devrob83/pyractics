#crear una lista con list
lista = list(["hola","Megan",3,True])
#devuelve la cantidad de elementos de una lista 
cantidad_de_elementos = len(lista)

#agregando elementos a a la lista 
agregando_con_append = lista.append("Damas")

#agregando elementos a a la lista en un indice especifico
lista.insert(2, "charlotte")

#agregando elementos a a la lista en un indice especifico
lista.extend([2, "charlotte", "hija", 2021, "rulos"])

#eliminando elementos de la lista en un indice especifico, -1para eliminiar el ultimo -2 el anteultimo y asi dependiendo del indice donde se encuentra
lista.pop(-2)

#eliminando elementos de la lista segun su valor
lista.remove(3)

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista de forma ascendente (si usamos el parametro reverse=true lo ordena en sentido contrario)
#lista.sort()

#invirtiendo los elementos de una lista 
lista.reverse()

#verificando si un elemento se encuentra en la lista 
elemento_encontrado = lista.index("Megan")

print(elemento_encontrado)