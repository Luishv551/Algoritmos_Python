import random

print('BEM VINDO AO JOGO DE ADIVINHAÇÃO\n')
print('================================================================\n')

number = random.randint(1, 100)
user_number = 0

while user_number != number:

    user_number = int(input('Guess a number between 1 and 100\n'))

    if user_number < number:
        print('Try again a bigger number')

    elif user_number > number:
        print('Try again a smaller number')

print(f'Congratulations, {number} is my number')


