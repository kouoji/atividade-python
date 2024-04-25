lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma_impares = 0

for i in lista_numeros:
    if i % 2 == 1:
        soma_impares += i

print(soma_impares)
