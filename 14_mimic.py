"""
14. mimic

Neste desafio você vai fazer um gerador de lero-lero.

É um programa que lê um arquivo, armazena a relação entre as palavras e
então gera um novo texto respeitando essas relações para imitar um
escritor de verdade.

Para isso você precisa:

A. Abrir o arquivo especificado via linha de comando.

B. Ler o conteúdo e separar as palavras obtendo uma lista de palavras.

C. Criar um dicionário de "imitação".

Nesse dicionário a chave será uma palavra e o valor será uma lista
contendo as palavras que aparecem no texto após a palavra usada na chave.

Por exemplo, suponha um arquivo com o conteúdo: A B C B A

O dicionário de imitação deve considerar que:
* a chave A contém uma lista com a palavra B
* a chave B contém uma lista com as palavras C e A
* a chave C contém uma lista com a palavra B

Além disso precisamos considerar que:
* a chave '' contém uma lista com a primeira palavra do arquivo
* a última palavra do arquivo contém uma lista com a palavra ''.

Com o dicionario imitador é bastante simples emitir aleatoriamente texto
que imita o original. Imprima uma palavra, depois veja quais palavras podem
vir a seguir e pegue uma aleatoriamente como a proxima palavra do texto.

Use a string vazia como a primeira palavra do texto para preparar as coisas.

Nota: o módulo padrão do python 'random' conta com o random.choice(list),
método que escolhe um elemento aleatório de uma lista não vazia.
"""

import random
import sys
import re


def get_words_from_file(filename):
    file = open(filename, "r")
    words = [word.upper() for line in file for word in re.split(r'\W+', line)]
    file.close()
    return words


def mimic_dict(filename):
    """Retorna o dicionario imitador mapeando cada palavra para a lista de
  palavras subsequentes."""
    # +++ SUA SOLUÇÃO +++
    words_from_file = get_words_from_file(filename)
    words = {"": [words_from_file[0]], words_from_file[-1]: [""]}
    for index, word in enumerate(words_from_file):
        if index < len(words_from_file) - 1:
            next_word = words_from_file[index + 1]
            if word in words.keys():
                if next_word not in words[word]:
                    words[word].append(next_word)
            else:
                words[word] = [next_word]
        else:
            continue
    return words


def print_mimic(mimic_dict, word):
    """Dado o dicionario imitador e a palavra inicial, imprime texto de 200 palavras."""
    # +++ SUA SOLUÇÃO +++
    first_word = mimic_dict[word][0]
    next_key = first_word
    text = [first_word]
    for i in range(199):
        next_key = random.choice(mimic_dict[next_key])
        text.append(next_key)
        
    print(" ".join(word for word in text))


# Chama mimic_dict() e print_mimic()
def main():
    if len(sys.argv) != 2:
        print('Utilização: ./14_mimic.py file-to-read')
        sys.exit(1)
    
    dict = mimic_dict(sys.argv[1])
    print_mimic(dict, '')


if __name__ == '__main__':
    main()
