
frutas = ["fresas","mango","piña","cambur","naranja"]
cadena = "Hola Robinson"
numeros = [9,8,1983,6,6,1981,8,2,2023]

#evitado que se coma un cambur con la sentencia continue
for fruta in frutas:
    if fruta == 'cambur':
        continue
    print(f'me voy a comer una {fruta}')
    
#evitar que el codigo siga ejecutandose   
for fruta in frutas:
    if fruta == 'piña':
        break
else:
    print("terminado")  
    
#recorrer una cadena de texto
for letra in cadena:
    print(letra)  
    
#for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)

#uso de for comun
numeros_triplicados = list()
for numero in numeros:
    numeros_triplicados.append(numero*3)
print(numeros_triplicados)

