#practicas de el if anidados elif
ingreso_mensual = 81000
gasto_mensual = 80000

if ingreso_mensual  > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print ("la llevas")    
    else:
        print ("estas gastanto demasiado")
    
elif ingreso_mensual > 1000:
    print ("Estas bien en latinoamerica")
    
elif ingreso_mensual > 800:
    print ("estas bien en argentina")
    
elif ingreso_mensual > 450:
    print ("puedes sobrevivir en venezuela")    
    
else:
    print ("pelaste bola")
