# Implementação do algoritmo Selection Sort
def selectionSort(array):
    # Laço externo que percorre o array
    for i in range(len(array)):
        # Inicializando a posição mínima como o próprio i
        min_idx = i
        # Laço interno para encontrar o menor elemento no restante do array
        for j in range(i + 1, len(array)):
            # Comparando o valor atual com o valor mínimo
            if array[j] < array[min_idx]:
                min_idx = j
        # Trocando o valor do menor elemento encontrado com o valor na posição i
        array[i], array[min_idx] = array[min_idx], array[i]

# Declaração de um array de números inteiros com 15 posições
array = [29, 10, 14, 37, 13, 25, 33, 67, 42, 58, 19, 46, 9, 51, 22]

# Exibindo o array original
print("Array original:")
print(array)

# Aplicando o algoritmo Selection Sort
selectionSort(array)

# Exibindo o array ordenado
print("\nArray ordenado com Selection Sort:")
print(array)
