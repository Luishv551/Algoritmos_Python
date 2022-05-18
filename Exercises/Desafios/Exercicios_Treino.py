Escreva um programa que recebe um número inteiro do usuário e responde se esse número é par ou não. Se um número é divisível por 2, ele é par.

numero = int(input('Vamos descobrir se esse número é par, digite seu numero aqui:\n'))

if (numero % 2) == 0:
    print ('Esse numero é par meu xara')
else:
    print('Puta velhote, esse numero ai nn e par nao hein')

a = int(input('Escreva aqui o primeiro lado do triangulo:\n'))
b = int(input('Escreva aqui o segundo lado do triangulo:\n'))
c = int(input('Escreve aqui o ultimo lado do triangulo:\n'))

if (a > b + c) or (c > a + b) or (b > a + c):
    print('Nao e um triangulo')
else:
    perimetro = (a + b + c) / 2
    area = (perimetro * (perimetro - a) * (perimetro - b) * (perimetro - c))**1/2
    print (f'A area do trinagulo e {area}')

print('Vamos jogar Pedra Papel Tesoura\n')
print('Digite [1] Para Pedra\n[2] Para Papel e [3] Para Tesoura ')

jog1 = int(input('Jogador 1, selecione a sua jogada:\n'))
jog2 = int(input('Jogador 2, selecione a sua jogada:\n'))

if jog1 == 1 and jog2 == 2:
    print('Jogador 2')
elif jog1 == 2 and jog2 == 1:
    print('Jogador 1')
elif jog2 == 1

name = input("Enter your name!\n")
print("Hello",name)

hours = int(input("Insert the total of hours\n"))
rate = int(input("Insert the total of rate\n"))

payment = hours * rate

print("Your payment is",payment,"U$")


lista = []
maior = 0
menor = 0
for i in range (0, 10):
    lista.append(int(input("Digite um número para a lista ")))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]

print(lista)
print("O maior valor é o",maior)
print("O menor valor é o", menor)

lista = []
for i in range (0, 5):
    lista.append(int(input("Digite um número para a lista ")))
media = sum(lista)/len(lista)

print(f'A média da sua lista é {media}')

listapar = []
listaimpar = []
lista = []
for i in range (0,5):
    lista.append(int(input("Digite um número para a lista ")))

for i in lista:
    if i % 2 == 0:
        listapar.append(i)
    else:
        listaimpar.append(i)

print (listapar)
print (listaimpar)

num = int(input('Digite um número e receba seu fatorial:\n'))
base = 1

for num in range(num, 0, -1):
    base =  num * base

print('O fatorial é {}'.format(base))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = int(input("Digite aqui o numero que deseja encontrar\n"))

if i not in lista:
    print("O numero desejado não está na lista")
else:
    num = lista.index(i)
    print(f"O número desejado está na posição {num}")

from collections import Counter

palavra = "Salameeeoouia"
tam_palavra = Counter(palavra)

for k, v in tam_palavra.items():
    if v > 1:
        print(f"A letra {k} está aparecendo mais de uma vez")

cont = 0
palavra_secreta = ["C", "U", "B", "O"]
letras_descobertas = []

print("\nJOGO DA FORCA\n")
for i in range(len(palavra_secreta)):
    letras_descobertas.append("-")

acertou = False



while acertou == False:

        letra = str(input("Digite uma Letra:\n"))

        for i in range(len(palavra_secreta)):
            if letra == palavra_secreta[i]:
                letras_descobertas[i] = letra
        acertou = True

        print(f"A palavra está assim: {letras_descobertas}")
      
    

    for x in range(len(letras_descobertas)):
        if letras_descobertas[x] == "-":
            acertou = False


myage = int(input("What's your age ?\n"))


print (f"You will be {myage + 1} in a year" )




