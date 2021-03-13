TuplaTelefonos=["3023465321","9876521"]
Diccionario={
    "Nombre":"Pablo",
    "Edad":17,
    "Ciudad":"Bogotá",
    "Sexo":"M",
    "Bachiller":False,
    "Telefonos":{
        "Celular":TuplaTelefonos[0],
        "Fijo":TuplaTelefonos[1]
        }
    }

def ImprimirDicionario(d):
    print(d)

def ModificarDiccionario(d, clave, valor):
    d[clave]=valor
    return d

def EliminarClave(d, clave):
    del d[clave]
    return d

def InfoDiccionario(d):
    print("Información Diccionario:\n")
    print(d.keys())
    print(d.values())
    print("Numero de claves:",len(d))

ImprimirDicionario(Diccionario)
Diccionario=ModificarDiccionario(Diccionario, "Nombre", "Diego")
ImprimirDicionario(Diccionario)
InfoDiccionario(Diccionario)
Diccionario=EliminarClave(Diccionario, "Sexo")
ImprimirDicionario(Diccionario)
print("Numero de Claves:", len(Diccionario))
