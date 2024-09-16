# Abrindo e lendo o conteúdo do arquivo "loremipsum.txt" utilizando open
file_path = 'loremipsum.txt'

# Abrindo o arquivo em modo de leitura
file = open(file_path, 'r')

# Lendo o conteúdo completo do arquivo
content = file.read()

# Imprimindo o conteúdo completo do arquivo
print("Conteúdo completo do arquivo:")
print(content)

# Imprimindo apenas a primeira linha do arquivo
file.seek(0)  # Volta para o início do arquivo
first_line = file.readline()
print("\nPrimeira linha do arquivo:")
print(first_line.strip())  # .strip() para remover espaços em branco extras

# Imprimindo apenas os 3 primeiros caracteres do arquivo
file.seek(0)  # Volta para o início do arquivo
three_chars = content[:3]
print("\nTrês primeiros caracteres do arquivo:")
print(three_chars)

# Fechando o arquivo
file.close()

# Utilizando a instrução with para abrir e ler o arquivo
with open(file_path, 'r') as file:
    # Lendo o conteúdo completo do arquivo novamente
    with_content = file.read()
    print("\nConteúdo completo do arquivo usando with:")
    print(with_content)
