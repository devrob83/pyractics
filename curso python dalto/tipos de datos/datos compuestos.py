#se pueden modificar los datos en las listas
lista = ["Robinson Padilla", "40", True, 1.71]
# no se pueden modificar los datos en las tuplas
tupla = ("Robinson Padilla", "40", True, 1.71)
#esto es valido
lista [3] = "enano"
#esto no es valido
#tupla [3] = "enano"

#creando un conjunto set "utiliza llaves"
#en los conjuntos, los datos repetidos no se muestran en pantalla, caso diferente que en las tuplas y las listas.
#tampoco almacena datos por indice como las otras dos opciones.
conjunto = {"Robinson Padilla", "40", True, 1.71, "40"}

#creando un diccionario (dict) (la estructura es key : value y se separan por comas)
diccionario = {
    'nombre' : "Charlotte",
    'edad' :"3",
    'es inteligente'  : "True",
    'hooby' : "pintar",
    'dato_duplicado' :"3"
}



