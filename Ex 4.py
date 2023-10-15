#4
i = 0
esf = 0
limp = 0
tro = 0
que = 0
porcent = 0
defeito = [["Necessita de esfera", esf, porcent],["Necessita de limpeza", limp, porcent],["Necessita troca do cabo ou conector", tro, porcent],["Quebrado ou inutilizado", que, porcent]]
ident = int
cont = 0
while ident != 0:
    ident = int(input("Id do erro?"))
    
    if ident == 1:
        defeito[0][1] = esf = esf + 1
        cont = cont + 1
        
    elif ident == 2:
        defeito[1][1] = limp = limp + 1
        cont = cont + 1
        
    elif ident == 3:
        defeito[2][1] = tro = tro + 1
        cont = cont + 1
        
    elif ident == 4:
        defeito[3][1] = que = que + 1
        cont = cont + 1
    else:
        print("Identificador errado.\n"
              "1 - Necessita de esfera\n"
              "2 - Necessita de limpeza\n"
              "3 - Necessita troca do cabo ou conector\n"
              "4 - Quebrado ou inutilizado\n"
              "0 - Finalizar\n")

defeito[0][2] = porcent = (esf * 100) / cont
defeito[1][2] = porcent = (limp * 100) / cont
defeito[2][2] = porcent = (tro * 100) / cont
defeito[3][2] = porcent = (que * 100) / cont
print("Quantidade de Mouses quebrados: ",cont)
while i < len(defeito):
    print(defeito[i])
    i = i + 1
