#2
salario = float
abono = float
lita1 = []
contar = 0
minimo = 0
colaboradores = 0
i = 0
while salario != 0:
    salario = float(input("salario?"))
    abono = salario * 0.2
    if salario > 0:
        if abono == 0:
            break

        elif  abono <= 100:
            lita1.append(["Salario: ", salario, "Abono: ", 100])
            contar = 100 + contar
            minimo = minimo + 1
            colaboradores = colaboradores + 1
        else:
            lita1.append(["Salario: ", salario, "Abono: ", abono])
            contar = abono + contar
            colaboradores = colaboradores + 1
    else:
        print("Salário inválido, tente um valor positivo.")
    
lita1.sort()
while i < len(lita1):
    print(lita1[i])
    i = i + 1
print("Foram processados", colaboradores, "colaboradores")
print("total de gastos com abono: ", contar)
print("Valor mínimo pago a ", minimo, "colaboradores")
print("Maior valor de abono pago:", lita1[-1][-1])
