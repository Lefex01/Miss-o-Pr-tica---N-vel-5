import time

# Função para ordenação usando Bubble Sort
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                
# Função para ordenação usando Selection Sort
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

# Função para medir o tempo de execução de uma função de ordenação
def measure_time(sort_function, array):
    start_time = time.time()
    sort_function(array)
    end_time = time.time()
    return end_time - start_time

# Leitura do arquivo e processamento do texto
def process_file(file_path):
    words = []
    with open(file_path, 'r') as file:
        for line in file:
            words.extend(line.split())
    return words

# Caminho do arquivo de entrada
file_path = 'texto.txt'

# Processa o arquivo
words = process_file(file_path)

# Ordena e mede o tempo usando Bubble Sort
words_bubble = words.copy()
bubble_sort_time = measure_time(bubble_sort, words_bubble)
print("Bubble Sort:")
print(words_bubble)
print(f"Tempo de execução: {bubble_sort_time:.6f} segundos")

# Ordena e mede o tempo usando Selection Sort
words_selection = words.copy()
selection_sort_time = measure_time(selection_sort, words_selection)
print("\nSelection Sort:")
print(words_selection)
print(f"Tempo de execução: {selection_sort_time:.6f} segundos")

# Ordena e mede o tempo usando o método nativo sort
words_native = words.copy()
start_time = time.time()
words_native.sort()
end_time = time.time()
native_sort_time = end_time - start_time
print("\nMétodo nativo sort:")
print(words_native)
print(f"Tempo de execução: {native_sort_time:.6f} segundos")

# Salvando o resultado final em um novo arquivo
with open('sorted_words.txt', 'w') as file:
    for word in words_native:
        file.write(word + '\n')
print("\nPalavras ordenadas salvas em 'sorted_words.txt'.")
