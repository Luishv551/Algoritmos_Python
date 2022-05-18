#Escreva uma função que recebe uma lista de elementos e retorne a quantidade de elementos únicos (distintos) na lista.
# def quant_elementos_distintos (elementos):
#     return len(set(elementos))

# print (quant_elementos_distintos([1,1,2,3,3,3,4,5,]))

# Escreva uma função que recebe uma lista de elementos e retorne a quantidade de elementos duplicados na lista.
# def quant_iguais(elementos):
#     return len(elementos) - len(set(elementos))

# print (quant_iguais ([1,1,1,1,2,2,3,3,3,4]))


# Escreva uma função que verifica se duas listas são iguais

def iguais ():
    l1 = []
    l2 = []
    
    print ('Preencha os valores da Lista 01')
    for n in range(0,3):
        l1.append ( int(input()) )
    
    print ('Preencha os valores da Lista 02')
    for n in range(0,3):
        l2.append ( int(input()) )

    print('\n')
    print (f'Lista 1: {l1}')
    print('\n')
    print (f'Lista 2: {l2}')
    
    l1.sort() 
    l2.sort() 
    if l1 == l2: 
        print ("As listas são identicas") 
    else : 
        print ("As listas não são identicas")
iguais()


