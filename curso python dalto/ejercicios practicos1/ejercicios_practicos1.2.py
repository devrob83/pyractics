#se le pide al usuario que diga una serie de frases
frase = input("Dime una frase y te calculare cuanto tiempo tardas en decirlo: ")

#se crea una lista con todas las palabras que contiene la frase ( y estas se cuentan por cada espacio que las separa)
palabras_separadas = frase.split(" ")

#se utiliza len() para ver la cantidad de elementos en la lista 
cantidad_de_palabras = len(palabras_separadas)

#en caso de que tarde mas de un minuto  en decir las palabras, se le dice que se detenga un poco   
if cantidad_de_palabras > 120:
    print("Loco amarrate la lengua halas mas que radio fiao")
    
#calculamos cuanto tarsaria en decir las palabras  y se lo decimos 
print(f'Dijiste {cantidad_de_palabras} Palabras, y tardarias {cantidad_de_palabras/2} segundos para decirlo')
print(f'EL dalto lo diria en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos para decirlo')