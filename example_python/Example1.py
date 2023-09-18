""" 
    Fecha: 18/09/2023
    Autor: Jeison velez
    Objetivo: """

import random

random_number = random.randint(1,10) #
print(random_number)

for i in range(0, 10):
    random_number = random.randrange(20, 100, 5)#Genra numero aleatorio entre un rango
    print(random_number)

print("--------------------------------")


for i in range (0, 10):
    random_number = random.random() #Genera numeros aleatorios con decimales
    print(random_number)

print("--------------------------------")

for i in range (0, 10):
    random_number = random.uniform(10.5, 20.6)  #Genera numerosa aleatorios partiendo de decimales
    print(random_number)

