#creando una funcion simple
#def saludar():
#    print("Hola pedazo de ..., como te va ?")
    
#saludar()
#creando una funcion que tenga parametros 
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = " Comandante"
    else:
        adjetivo = 'maricon'
    
    
    print(f"Hola {nombre}, {adjetivo} ¿Como estas?")
    
saludar("Evelyn","MuJer")
saludar("Robinson", "hombre")
saludar("Marcelo", "cosa")

#crear ua funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghijklmno"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]},{num*2}"
    return(contraseña,num)
#desempaquetando la funcion
password,primer_numero = crear_contraseña_random(981)
#mostrando los datos obtenidos y utilizados para obtenerla
print(f'tu nueva contraseña es: {password}')
print(f'el numero utilizado para crearla fue: {primer_numero}') 







        
#def frase(nombre, apellido,adjetivo):
#    return f'Hola {nombre} {apellido}, eres muy {adjetivo}'

#frase_resultante = frase("Megan","Damas","Tremenda") 
#print(frase_resultante)