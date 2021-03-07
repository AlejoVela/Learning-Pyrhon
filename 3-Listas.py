ListaNombres = ["Maria", "Marta", "Antonio", "Jose"]

def AccedientoATodaLaLista():
    print("Toda esta lista es: ", ListaNombres)

def AccedientoAUnItemEspecifico(pos):
    print("El item accedido es ",ListaNombres[pos], " y esta en la posción ", pos)

def AñadiendoElementoAlFinalDeLista(Elemento):
    ListaNombres.append(Elemento)
    print("Se ha añadido '", Elemento, "' a la lista")

def AñadiendoElementoPorPosicionLista(pos ,Elemento):
    ListaNombres.insert(pos , Elemento)
    print(Elemento, " ah sido añadido en la posicion ", pos, " de la lista")

def UnirListas(lista1, lista2):
    lista1.extend(lista2)
    return lista1

def MostrandoIndiceElementoLista(Elemento):
    print(Elemento, "Se encuentra en la posicion ", ListaNombres.index(Elemento), " de la lista")

def ComprobarSiElementoExisteLista(Elemento):
    if(Elemento in ListaNombres):
        print(Elemento, " se encuentra actualmente registrado en la lista")
    elif(Elemento not in ListaNombres):
        print(Elemento, " no se encuentra actualmente registrado en la lista")
    else:
        print("No se llego a una conclusión")

def EliminarElementoLista(Elemento):
    ListaNombres.remove(Elemento)
    print("Se ha eliminado el elemento '", Elemento, "' de la lista")
    return ListaNombres

def RepitiendoListaConOperadoPor(Lista,numerRepeticiones):
    ListaLocal = Lista* numerRepeticiones
    return ListaLocal

    
AccedientoATodaLaLista()

AccedientoAUnItemEspecifico(0)

AñadiendoElementoAlFinalDeLista("Mayerly")

AñadiendoElementoPorPosicionLista(0, "Diego")

AccedientoATodaLaLista()

ListaNombres = UnirListas(ListaNombres, ["El Cara flauta", "La lora", "Me gane mil pesos"])

AccedientoATodaLaLista()

MostrandoIndiceElementoLista("Antonio")

ComprobarSiElementoExisteLista("Mayerly")

EliminarElementoLista("Diego")

AccedientoATodaLaLista()

ListaNombres = RepitiendoListaConOperadoPor(ListaNombres, 2)

AccedientoATodaLaLista()


