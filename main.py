import random

element = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
tamano = int(input("elige cuantos caracteres tendra la contraseña"))

password = ""

for i in range(tamano):
    password += random.choice(element)

print("contraseña:", password)
