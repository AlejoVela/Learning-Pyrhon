Numero1 = 2
Numero2 = 5
Numero3 = 5.6

def NoRecibeNoRetorna():
    print("El resultado de la suma de ", str(Numero1), " + ",str(Numero2), " es: ")

def RecibeYRetorna(Num1, Num2):
    
    Sum = Num1 + Num2
    return Sum

def NoRecibeYRetorna():
    print("Pero, si este resultado se sumara con ", str(Numero3))

def RecibeNoRetorna(Res1, Num3):
    print("El Resultado sería: ")
    Sum = Res1 + Num3
    print(Sum)


NoRecibeNoRetorna()
Resultado1 = RecibeYRetorna(Numero1, Numero2)
print(Resultado1)
NoRecibeYRetorna()
RecibeNoRetorna(Resultado1, Numero3)


    
