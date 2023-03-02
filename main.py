import random
letters = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
symbols = ["!", "@", "#", "$", "%", "&", "+", "?"]

print("Seja bem vindo(a) ao gerador de senhas 3000, atualizado 2023")
nr_letters = int(input("quantas letra vc quer? "))
nr_symbols = int(input(f"quantos simbolos vc quer? "))
nr_numbers = int(input(f"quantos numeros vc quer? "))

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"A sua senha é: {password}")