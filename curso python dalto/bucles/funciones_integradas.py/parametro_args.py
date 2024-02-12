#forma no optima de sumar valores
#def suma(lista):
#    numeros_sumados = 0
#    for numero in lista:
#        numeros_sumados = numeros_sumados + numero
#    return numeros_sumados    

#resultado = suma([5,3,9,10,20,3])

#utilizando el parametro args
def suma(nombre,*numeros):
    return f"{nombre},la suma de tus numeros es : {sum(numeros)}"

resultado = suma("Megan",4,5,6,7,9,11,54)
print(resultado)