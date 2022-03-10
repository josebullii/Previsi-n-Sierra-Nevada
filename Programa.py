def leerDatos ():
    f = open ("Prevision.txt", "r")
    vDatos = []

    for linea in f:
        vDatos.append(linea)
    f.close()
    return vDatos

def diasSoleados (vDatos):
    for dato in vDatos:
        datos = dato.split("-")
        
        if datos[1] == "Soleado" or datos[1] == "Soleado\n":
            print("El día", datos[0], "será soleado")

def diasNieve (vDatos):
    for dato in vDatos:
        datos = dato.split("-")

        if datos[1] == "Nieve":
            print("El día", datos[0], "será de nieve y caerá", datos[2], "de nieve")
    print("Se acumularán un total de 20cm de nieve")

#Programa
vDatos = leerDatos ()
print (vDatos)

diasSoleados (vDatos)
diasNieve (vDatos)