#creando una funcion simple
#def saludar():
#    print("Hola buenos dias, listo para aprender?")
#ejecutando la funcion simple    
#saludar()

#crear una funcion que tenga parametros
def saludar(nombre,sexo):
    sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "reina"
    elif(sexo == "hombre"):
        adjetivo = "pana"
    else:
        adjetivo = 'amor'
    print(f'Hola {nombre},mi {adjetivo} Como estas hoy?')
    
saludar("Robinson","hombre")
saludar("megan","mujer")
saludar("Evelyn","undefined")

#crear una funcion que nos retorne valores
def crear_contraseña_ramdom(num):
    chars = "abcdefhij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num
#desempaquetando la funcion
password,primer_numero = crear_contraseña_ramdom(718)
#mostrando los resultados obtenidos y los datos utilizados para obtenerlos
print(f"Tu contraseña nueva es: {password}")
print(f"el numero utilizado para crearla fue: {primer_numero}")
