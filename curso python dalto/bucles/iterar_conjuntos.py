animales = {"gato","perro","mono", "chiguire"}
numeros = {3,8,5,15}

#recorriendo la conjunto "animales"
for animal in animales:
    print(f'ahora la variable animal es igual a:{animal}')
    
#recorriendo la conjunto y multiplicando cada valor por 10    
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#iterando dos conjuntos del mismo tamaño al mismo tiempo    
for numero,animal in zip(animales,numeros):
    print(f"Recorriendo conjunto 1:{numero}")
    print(f"Recorriendo conjunto 2:{animal}")
    
    
#forma correcta de recorrer una conjunto con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
print(f'el indice es {indice} el valor es {valor}')

#usando el for/else
for numero in numeros:
    print(f'ejecutando el utlimo bucle, valor actual: {numero}')
else:
    print("el bucle termino")


# lo anterior funciona exactamente igual para las tuplas  y listas  

