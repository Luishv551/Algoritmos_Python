#Cifra de Cesar básico

# def cifra_de_cesar(chave, letra):
#     print(ord(letra))
#     print(ord(letra) + chave)
#     return chr(ord(letra) + chave)

# entrada = 'a'
# resposta = cifra_de_cesar(3, entrada)

# print(f'A Cifra de Cesar de {entrada} é {resposta}')

# import string
# plain_text = "aaa"
# shift = 1

# alphabet = string.ascii_lowercase
# shifted = alphabet[0:]

# table = str.maketrans(alphabet, shifted)
# encrypted = plain_text.translate(table)

# print (encrypted)

alphabet = "abcdefghijklmnopqrstuvwxyz"
user_message = input("Enter your secret message: \n")
user_message = user_message.lower()
key = int(input("Enter your secret key: \n"))
new_message = ""

for character in user_message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position + key) % 26
        new_character = alphabet[new_position]
        new_message += new_character

print ("Your new message is " + new_message)