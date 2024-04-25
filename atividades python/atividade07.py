valores = [10, 20, 30, 40, 50]

soma = 0

for valor in valores:
    soma += valor

media = 0

try:
    media = soma / len(valores)
except ZeroDivisionError:
    print("Erro: A lista está vazia. Não é possível calcular a média.")

print("A média dos valores na lista é:", media)
