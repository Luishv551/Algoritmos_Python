# Escreva um programa que recebe um número inteiro do usuário e responde se esse número é par ou não. Se um número é divisível por 2, ele é par.

# numero = int(input('Vamos descobrir se esse número é par, digite seu numero aqui:\n'))

# if (numero % 2) == 0:
#     print ('Esse numero é par meu xara')
# else:
#     print('Puta velhote, esse numero ai nn e par nao hein')

# a = int(input('Escreva aqui o primeiro lado do triangulo:\n'))
# b = int(input('Escreva aqui o segundo lado do triangulo:\n'))
# c = int(input('Escreve aqui o ultimo lado do triangulo:\n'))

# if (a > b + c) or (c > a + b) or (b > a + c):
#     print('Nao e um triangulo')
# else:
#     perimetro = (a + b + c) / 2
#     area = (perimetro * (perimetro - a) * (perimetro - b) * (perimetro - c))**1/2
#     print (f'A area do trinagulo e {area}')

# print('Vamos jogar Pedra Papel Tesoura\n')
# print('Digite [1] Para Pedra\n[2] Para Papel e [3] Para Tesoura ')

# jog1 = int(input('Jogador 1, selecione a sua jogada:\n'))
# jog2 = int(input('Jogador 2, selecione a sua jogada:\n'))

# if jog1 == 1 and jog2 == 2:
#     print('Jogador 2')
# elif jog1 == 2 and jog2 == 1:
#     print('Jogador 1')
# elif jog2 == 1

# name = input("Enter your name!\n")
# print("Hello",name)

# hours = int(input("Insert the total of hours\n"))
# rate = int(input("Insert the total of rate\n"))

# payment = hours * rate

# print("Your payment is",payment,"U$")


# lista = []
# maior = 0
# menor = 0
# for i in range (0, 10):
#     lista.append(int(input("Digite um número para a lista ")))
#     if i == 0:
#         maior = menor = lista[i]
#     else:
#         if lista[i] > maior:
#             maior = lista[i]
#         if lista[i] < menor:
#             menor = lista[i]

# print(lista)
# print("O maior valor é o",maior)
# print("O menor valor é o", menor)

# lista = []
# for i in range (0, 5):
#     lista.append(int(input("Digite um número para a lista ")))
# media = sum(lista)/len(lista)

# print(f'A média da sua lista é {media}')

# listapar = []
# listaimpar = []
# lista = []
# for i in range (0,5):
#     lista.append(int(input("Digite um número para a lista ")))

# for i in lista:
#     if i % 2 == 0:
#         listapar.append(i)
#     else:
#         listaimpar.append(i)

# print (listapar)
# print (listaimpar)

# num = int(input('Digite um número e receba seu fatorial:\n'))
# base = 1

# for num in range(num, 0, -1):
#     base =  num * base

# print('O fatorial é {}'.format(base))

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = int(input("Digite aqui o numero que deseja encontrar\n"))

# if i not in lista:
#     print("O numero desejado não está na lista")
# else:
#     num = lista.index(i)
#     print(f"O número desejado está na posição {num}")

# from collections import Counter

# palavra = "Salameeeoouia"
# tam_palavra = Counter(palavra)

# for k, v in tam_palavra.items():
#     if v > 1:
#         print(f"A letra {k} está aparecendo mais de uma vez")

# cont = 0
# palavra_secreta = ["C", "U", "B", "O"]
# letras_descobertas = []

# print("\nJOGO DA FORCA\n")
# for i in range(len(palavra_secreta)):
#     letras_descobertas.append("-")

# acertou = False



# while acertou == False:

#         letra = str(input("Digite uma Letra:\n"))

#         for i in range(len(palavra_secreta)):
#             if letra == palavra_secreta[i]:
#                 letras_descobertas[i] = letra
#         acertou = True

#         print(f"A palavra está assim: {letras_descobertas}")
      
    

#     for x in range(len(letras_descobertas)):
#         if letras_descobertas[x] == "-":
#             acertou = False

# import random
# import string
# from words import words



# def get_valid_word(words):
#     word = random.choice(words) #It will get some random word from words
#     while '-' in word or ' ' in word: #Loop because we want a game that can play a lot of words
#         word = random.choice(words) #Keep getting words
#     return word

# def hangman(): 
#     word = get_valid_word(words)
#     word_letters = set(word) #letters in the word
#     alphabet = set(string.ascii_uppercase) #alphabet
#     used_letters = set() #Track all the words that the use add new words

#     #getting user input
#     while len(word_letters) > 0:
#         #letters used
#         print('You have used these letters: ', ' '.join(used_letters))
#         #What the current word is (A - B - A - C)
#         word_list = [letter if letter in used_letters else '-' for letter in word]
#         user_letter = input('Guess a letter:\n').upper()
#         if user_letter in alphabet - used_letters:
#             used_letters.add(user_letter)
#             if user_letter in word_letters:
#                 word_letters.remove(user_letter)
#         elif user_letter in used_letters:
#             print ('You already used this character, please try again.\n')
#         else:
#             print ('This character is not in the alphabet, please try again.\n') 

# hangman()   


# import random
# from words import words
# from hangman_visual import lives_visual_dict
# import string


# def get_valid_word(words):
#     word = random.choice(words)  # randomly chooses something from the list
#     while '-' in word or ' ' in word:
#         word = random.choice(words)

#     return word.upper()


# def hangman():
#     word = get_valid_word(words)
#     word_letters = set(word)  # letters in the word
#     alphabet = set(string.ascii_uppercase)
#     used_letters = set()  # what the user has guessed

#     lives = 7

#     # getting user input
#     while len(word_letters) > 0 and lives > 0:
#         # letters used
#         # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
#         print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

#         # what current word is (ie W - R D)
#         word_list = [letter if letter in used_letters else '-' for letter in word]
#         print(lives_visual_dict[lives])
#         print('Current word: ', ' '.join(word_list))

#         user_letter = input('Guess a letter: ').upper()
#         if user_letter in alphabet - used_letters:
#             used_letters.add(user_letter)
#             if user_letter in word_letters:
#                 word_letters.remove(user_letter)
#                 print('')

#             else:
#                 lives = lives - 1  # takes away a life if wrong
#                 print('\nYour letter,', user_letter, 'is not in the word.')

#         elif user_letter in used_letters:
#             print('\nYou have already used that letter. Guess another letter.')

#         else:
#             print('\nThat is not a valid letter.')

#     # gets here when len(word_letters) == 0 OR when lives == 0
#     if lives == 0:
#         print(lives_visual_dict[lives])
#         print('You died, sorry. The word was', word)
#     else:
#         print('YAY! You guessed the word', word, '!!')


# if __name__ == '__main__':
#     hangman()


#3 Tentastiva

import random

words = ['cat', 'dog', 'bird', 'fish', 'earth']

hangman_graphics = ['_',
                    '__',
                    '__\n |',
                    '__\n |\n O',
                    '__\n |\n O\n |',
                    '__\n |\n O\n/|',
                    '__\n |\n O\n/|\ ',
                    '__\n |\n O\n/|\ \n/',
                    '__\n |\n O\n/|\ \n/ \ '                
                    ]

number_mistakes = 0
letters_guessed = []
number_mistakes_allowed = len(hangman_graphics)
word = random.choice(words)
letters_word = list(word)
wrong_letters = []

print()
print('The word has {} letters.\n'.format(len(word))) 

while number_mistakes < number_mistakes_allowed:
    print()
    print('Wrong Letters: ', end = '')
    for letter in wrong_letters:
        print('{}, '.format(letter), end = '')
    print()
    print('Guesses left: {}'.format(number_mistakes_allowed - number_mistakes))
    letter_user = input('Please enter a letter --> ')

    while letter_user in letters_guessed or letter_user in wrong_letters:
        print()
        print('You have already guessed this lettter, enter another one')
        letter_user = input('Enter a letter --> ')

    if letter_user not in letters_word:
        number_mistakes += 1
        wrong_letters.append(letter_user)

    print()
    print('Word: ', end = '')

    for letter in letters_word:
        if letter_user == letter or letter_user == word:
            letters_guessed.append(letter_user)
    
    for letter in letters_word:
        if letter in letters_guessed:
            print(letter + ' ', end = '')
        else:
            print('_', end = '')
    
    print()
    if number_mistakes:
        print(hangman_graphics[number_mistakes - 1])

    print()
    print('-----------------------------------------')

    if len(letters_guessed) == len(letters_word):
        print()
        print('YOU WON')
        break
if number_mistakes == number_mistakes_allowed:
    print()
    print('YOU LOST TRY AGAIN\n')
    print('The word was {}'.format(word)
