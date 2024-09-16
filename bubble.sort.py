# Implementação do algoritmo Bubble Sort
def bubbleSort(array):
    # Laço externo que percorre o array
    for i in range(len(array)):
        # Laço interno que compara elementos adjacentes
        for j in range(0, len(array) - i - 1):
            # Verifica se o elemento atual é maior que o próximo
            if array[j] > array[j + 1]:
                # Realiza a troca dos elementos
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

# Declaração de um array de números inteiros com 15 posições
array = [64, 34, 25, 12, 22, 11, 90, 78, 23, 56, 43, 67, 89, 12, 34]

# Exibindo o array original
print("Array original:")
print(array)

# Aplicando o algoritmo Bubble Sort
bubbleSort(array)

# Exibindo o array ordenado
print("\nArray ordenado com Bubble Sort:")
print(array)
