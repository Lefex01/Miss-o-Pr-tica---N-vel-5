# Ordenação de um array de inteiros
# Criação do array de 15 posições com números inteiros aleatórios
integers_array = [34, 7, 23, 32, 5, 62, 31, 18, 9, 50, 27, 41, 12, 22, 45]

# Ordenando o array em ordem crescente
integers_array.sort()
print("Array ordenado em ordem crescente:")
print(integers_array)

# Ordenando o array em ordem decrescente
integers_array.sort(reverse=True)
print("\nArray ordenado em ordem decrescente:")
print(integers_array)

# Criação de um array de strings (nomes, datas de nascimento, CPF e RG)
strings_array = ["Lucas", "2000-05-15", "123.456.789-10", "45.678.901-2",
                 "Julia", "1995-07-22", "987.654.321-00", "23.456.789-1"]

# Ordenando o array de strings em ordem crescente (alfabética)
strings_array.sort()
print("\nArray de strings ordenado em ordem crescente:")
print(strings_array)

# Ordenando o array de strings em ordem decrescente
strings_array.sort(reverse=True)
print("\nArray de strings ordenado em ordem decrescente:")
print(strings_array)

