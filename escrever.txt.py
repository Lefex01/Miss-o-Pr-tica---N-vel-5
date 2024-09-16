# Criando uma lista com frases
texto = list()
texto.append("Esta é a primeira frase do arquivo.")
texto.append("Aqui está a segunda frase que estamos adicionando.")
texto.append("E esta é a terceira frase que será escrita no arquivo.")

# Abrindo o arquivo "texto.txt" em modo de escrita
with open('texto.txt', 'w') as file:
    # Escrevendo cada frase da lista no arquivo
    for linha in texto:
        file.write(linha + '\n')

print("Dados foram escritos no arquivo 'texto.txt'.")
