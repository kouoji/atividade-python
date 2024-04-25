# Create a list of numbers
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize the sum variable
soma = 0

# Use a for loop to iterate through the list of numbers
for numero in numeros:
    try:
        # Try to convert the number to an integer and add it to the sum
        soma += int(numero)
    except ValueError:
        # If the conversion fails, print an error message
        print(f"Não foi possível converter o número {numero} para um número inteiro.")

# Print the sum
print(f"A soma dos números é {soma}.")