numeros = [10, 20, 30, 40, 50]

soma = 0

for numero in numeros:
    try:
        soma += numero
    except TypeError:
        print("Erro: Um dos elementos da lista não é um número.")

print("A soma de todos os elementos é:", soma)
