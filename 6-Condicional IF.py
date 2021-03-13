lista = [1,2,3,4,5]

def sumarDatosLista(l, pos, dato):
    if (l[pos] > dato):
        print('El dato ',l[pos], ' es mayor al dato de la lista con valor ',dato)
    elif(l[pos]<dato):
        print('el dato',l[pos], 'es menor al dato de la lista con valor ',dato)
    else:
        print('Los datos son iguales y valen ',dato)

sumarDatosLista(lista, 3, 3)
