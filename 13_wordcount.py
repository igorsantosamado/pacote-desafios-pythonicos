"""
13. wordcount

Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.

A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.

Por exemplo:

$ python wordcount.py --count letras.txt
a 2
b 4
c 3

B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.

Ou seja...

Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.

Por exemplo:

$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2

Abaixo já existe um esqueleto do programa para você preencher.

Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.

Seu trabalho é implementar as funções print_words() e depois print_top().

Dicas:
* Armazene todas as palavras em caixa baixa, assim, as palavras 'A' e 'a'
  contam como a mesma palavra.
* Use str.split() (sem parêmatros) para fazer separar as palavras.
* Não construa todo o programade uma vez. Faça por partes executando
e conferindo cada etapa do seu progresso.
"""

import sys


# +++ SUA SOLUÇÃO +++
# Defina as funções print_words(filename) e print_top(filename).

def get_chars_from_file(filename):
    f = open(filename, 'r')
    list_chars = [char.upper() for line in f for char in line.split()]
    f.close()
    return list_chars


def get_chars_count(chars):
    return {char: chars.count(char) for char in dict.fromkeys(chars)}


def print_chars(chars, reverse=False, sorted_by="key", qty="all"):
    dict_char_count_sorted = {key: count for key, count in sorted(chars.items(),
                                                                  key=lambda item: item[
                                                                      0 if sorted_by == "key" else 1
                                                                      if sorted_by == "value" else 0],
                                                                  reverse=reverse)}

    for char, count in list(dict_char_count_sorted.items())[: None if qty == "all" else qty]:
        print(f"{char} {count}")


def print_words(filename):
    list_chars = get_chars_from_file(filename)
    dict_char_count = get_chars_count(list_chars)

    print_chars(dict_char_count)


def print_top(filename):
    list_chars = get_chars_from_file(filename)
    dict_char_count = get_chars_count(list_chars)

    print_chars(dict_char_count, True, "value", 20)


# A função abaixo chama print_words() ou print_top() de acordo com os
# parêtros do programa.
def main():
    if len(sys.argv) != 3:
        print('Utilização: ./13_wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
