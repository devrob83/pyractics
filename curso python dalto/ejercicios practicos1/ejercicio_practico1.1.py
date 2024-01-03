#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_dalto = 1.5

#duracion de crudos(tiempo sin edicion o sobrante )
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de duracion
diferencia_con_min = 100 - curso_dalto / otros_cursos_min * 100 
diferencia_con_max = 100 - curso_dalto * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - curso_dalto / otros_cursos_promedio * 100 

#calculando el porcentaje de tiempo removido

tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - curso_dalto * 1000 // crudo_dalto / 10

#mostrando las diferencias de duracion (ejercicio a)
print("----------------------")
print(f'el curso de dalto dura un:')
print(f' - un {diferencia_con_min}% menos que el curso mas rapido de la competencia')
print(f' - un {diferencia_con_promedio}% menos que el curso promedio de la competencia')
print(f' - un {diferencia_con_max}% menos que el curso mas largo de la competencia')
print("----------------------")

#mostrando la cantidad de espacios vacios que se remueven  (ejercicio b)
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'este curso elimino un {tiempo_vacio_dalto}% de tiempo vacio')
print("----------------------")

#mostrando diferencias si los cursos duraran 10 horas 
print(f'ver 10 horas de este curso equivale a ver{otros_cursos_promedio* 100 // curso_dalto / 10}% horas de otros cursos')
print(f'ver 10 horas de otros cursos equivale a ver{curso_dalto* 100 // otros_cursos_promedio / 10}% horas de este curso')
print("----------------------")
