
import random

Lista1 = []

for i in range(10):
    Lista1.append(random.randint(1, 10))

print("La primera lista creada es: ", Lista1)

Lista2 = []

for j in Lista1:
    Lista2.append(j**3)

print("Los cubos de la primera lista son: ", Lista2)

Lista3 = []

for k in Lista1:
    Lista3.append(k**2)

print("Los cuadrados de la primera lista son: ", Lista3)

ListaConcat = Lista2 + Lista3
ListaConcat.reverse()

print("La suma de los dos listas de manera inversa es: ", ListaConcat)

