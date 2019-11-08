#Creacion1
registro ={"Carlos": 20, "Dennis": 15, "Sheyla": 14, "Fabrizio":18}
print("registro es : ", (registro))
texto = "Fabrizio"
#Pertenencia1
if ( texto in registro ):
    print("el key '", texto, "' si existe en dict registro")
else:
    print("el key '", texto, "' NO existe en dict registro")
if ( "Juan" not in registro ):
    print("key 'Juana' no esta en dict registro")
#Comparacion1
print ("registro['Carlos']== registro['Dennis'] => ", registro['Carlos']== registro['Dennis'])
print ("registro['Carlos']== registro['Dennis'] => ", registro['Carlos']!= registro['Dennis'])
#Indexacion1
print(registro["Carlos"])
print(registro["Dennis"])
print(registro["Sheyla"])
print(registro["Fabrizio"])
# Iteracion1
print("Listado de claves")
for key in registro:
    print(key)

print("Listado de valores")
for key in registro:
    print(registro[key])

print("Listado de clave - valor")
for k,v in zip(registro.keys(), registro.values()):
    print(k, v)

print("Listado de clave - valor con items()")
for k,v in registro.items():
    print(k,v)
#BUSQUEDA1
#buscar clave
print(registro.get("Carlos"))
print(registro.get("Dennis"))
print(registro.get("nota5"))

# Comprobar si no existe la clave
if ( registro.get("nota5") == None):
    print("La nota5 no existe")
#reemplazo1
print("Carlos:", registro["Carlos"])
print("Dennis:", registro["Dennis"])
# Hacemos el reemplazo de carlos y Dennis
registro["Carlos"] = "Cesar"
registro["Dennis"] = "Manuel"

print("despues del reemplazo:", registro["Carlos"])
print("despues del reemplazo:",registro["Dennis"])
#eliminacion1
del registro["Dennis"]
print(registro.get("Dennis"))
del registro
print(registro)

#Creacion2
DNI ={"Agustin":16670245 , "Jerson": 72498428, "Melissa":12345432 , "Rosa":18432122}
print("DNI es : ", (DNI))
texto = "Rosa"

#Pertenencia2
if ( texto in DNI ):
    print("el key '", texto, "' si existe en dict DNI")
else:
    print("el key '", texto, "' NO existe en dict DNI")
if ( "FERNANDO" not in DNI ):
    print("key 'Juana' no esta en dict DNI")
#Comparacion2
print ("DNI['Agustin']== DNI['Jerson'] => ", DNI['Agustin']== DNI['Jerson'])
print ("DNI['Agustin']== DNI['Rosa'] => ", DNI['Agustin']!= DNI['Rosa'])
#Indexacion2
print(DNI["Agustin"])
print(DNI["Rosa"])
print(DNI["Jerson"])
print(DNI["Melissa"])
# Iteracion2
print("Listado de claves")
for key in DNI:
    print(key)

print("Listado de valores")
for key in DNI:
    print(DNI[key])

print("Listado de clave - valor")
for k,v in zip(DNI.keys(), DNI.values()):
    print(k, v)

print("Listado de clave - valor con items()")
for k,v in DNI.items():
    print(k,v)
#BUSQUEDA2
#buscar clave
print(DNI.get("Agustin"))
print(DNI.get("Rosa"))
print(DNI.get("Jhair"))

# Comprobar si no existe la clave
if ( DNI.get("Anderson") == None):
    print("El DNI no existe")
#reemplazo2
print("Agustin:", DNI["Agustin"])
print("Melissa:", DNI["Melissa"])
# Hacemos el reemplazo
DNI["Agustin"] = "Zoila"
DNI["Melissa"] = "Lola"

print("despues del reemplazo:", DNI["Zoila"])
print("despues del reemplazo:",DNI["Lola"])
#eliminacion2
del DNI["Jerson"]
print(DNI.get("Jerson"))
del DNI
print(DNI)

#Creacion3
mercado ={"pollo": "1/2 kilo", "Carne": "1 kilo", "Papas": "3 kilos"}
print("registro es : ", (registro))
texto = "jamon"
#Pertenencia3
if ( texto in registro ):
    print("el key '", texto, "' si existe en dict mercado")
else:
    print("el key '", texto, "' NO existe en dict mercado")
if ( "pescado" not in registro ):
    print("key 'pescado' no esta en dict registro")
#Comparacion3
print ("mercado['pollo']== mercado['carne'] => ", mercado['pollo']== mercado['carne'])
print ("mercado['pollo']== mercado['papas'] => ", mercado['pollo']!= mercado['papas'])
#Indexacion3
print(mercado["pollo"])
print(mercado["papas"])
print(mercado["carne"])
# Iteracion3
print("Listado de claves")
for key in mercado:
    print(key)

print("Listado de valores")
for key in mercado:
    print(mercado[key])

print("Listado de clave - valor")
for k,v in zip(mercado.keys(), mercado.values()):
    print(k, v)

print("Listado de clave - valor con items()")
for k,v in mercado.items():
    print(k,v)
#BUSQUEDA3
#buscar clave
print(mercado.get("Carne"))
print(mercado.get("Pollo"))
print(mercado.get("Huevos"))

# Comprobar si no existe la clave
if ( mercado.get("huevos") == None):
    print("Los huevos no se encuentran en la lista de mercado")
#reemplazo3
print("pollo:", mercado["pollo"])
print("carne:", mercado["carne"])
# Hacemos el reemplazo de pollo y carne
mercado["pollo"] = "cebollas"
mercado["carne"] = "limones"

print("despues del reemplazo:", mercado["pollo"])
print("despues del reemplazo:",mercado["carne"])
#eliminacion3
del mercado["Dennis"]
print(mercado.get("Dennis"))
del mercado
print(mercado)
