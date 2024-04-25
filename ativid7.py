# Create a list of numbers
numeros = [1, 2, 3, 4, 5]

# Initialize the sum variable
soma = 0

# Use a for loop to iterate through the list of numbers
for numero in numeros:
    soma += numero

# Calculate the average
try:
    media = soma / len(numeros)
except ZeroDivisionError:
    print("Não é possível calcular a média de uma lista vazia.")

# Print the average
print(f"A média dos números é {media}.")