# Se define la tupla con parentesis a diferencia de los corchetes de la lista
miTupla=("Enero",22," del 2021")


def ContarElementosTupla():
    Numero = miTupla.count()
    return Numero

def ConvertirTuplaALista(tupla):
    miLista = list(tupla)
    print("La tupla: '", tupla, "' ha sido convertida a una Lista '", miLista, "'")

def ConvertirListaATupla(lista):
    tupla = tuple(lista)
    print("La lista: '", lista, "' ha sido convertida a una tupla: '", tupla, "'")

def DescomposicionDeTuplas(tupla):
    mes, dia, año = tupla
    print("La fecha es ", dia, " de ", mes, año)

print("Mi tupla tiene ", miTupla, " elementos")
ConvertirTuplaALista(miTupla)
ConvertirListaATupla(["Holiwis", "Me iamo miguel"])
DescomposicionDeTuplas(miTupla)
