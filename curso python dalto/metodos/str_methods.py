cadena1 = "Hola soy Megan"
cadena2 = " Soy una niña"

#convierte a mayuscula
mayuscula = cadena1.upper()

#convierte a minuscula
rminuscula = cadena1.lower()

#convierte primera letra a mayuscula
primera_letra_mayuscula = cadena1.capitalize()

#busca una cadena con otra cadena, si no hay coincidencias, se mostrara -1
busqueda_find = cadena1.find("soy")

#busca una cadena en otra cadena, si no hay coincidencias muestra despliega error del tipo exepciones
busqueda_index = cadena1.index("s")

#si es numerico devuelve true, si no es numerico devuelve false
es_numerico = cadena1.isnumeric()

#si es alfanumerico devuelve true, si no es numerico devuelve false, si contiene caracteres especiales o espacios lo declara falso autamaticamente por no estar entre los caracteres alfabeticos
es_alfanumerico = cadena1.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("o")

#contamos cuantos caracteres posee una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("H")

#vierificamos si una cadena termina con otra cadena dada, si es asi devuelve true 
termina_con = cadena1.endswith("n")

#reemplaza un pedazo de la cadena dada, por otra dada 
cadena_nueva = cadena1.replace("Megan","Robinson")

#separa cadenas con la cadena que le pasemos  
cadena_separada = cadena1.split(" ")


print(type(cadena_separada))
