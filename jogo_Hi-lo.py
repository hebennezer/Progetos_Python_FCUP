from random import *

number = randint(1, 100)
guess = 0
tentativas = 0

while guess != number:
    tentativas += 1
    guess = int(input("Escreva um número 1-100: "))

    if guess > number:
        print("é menor.")
    elif guess < number:
        print("é maior")
    
print(guess, " é correto")
print(tentativas, " tentatisvas")