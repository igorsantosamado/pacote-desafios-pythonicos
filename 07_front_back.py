"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""


def front_back(a, b):
    # +++ SUA SOLUÇÃO +++
    front_a = manage_char_split(a, 'front')
    back_a = manage_char_split(a, 'back')
    front_b = manage_char_split(b, 'front')
    back_b = manage_char_split(b, 'back')

    return "".join([front_a, front_b, back_a, back_b])


def manage_char_split(string, position='front'):
    string_to_return = ""
    if position == "front":
        string_to_return = string[:len(string) // 2 if len(string) % 2 == 0 else ((len(string) // 2) + 1)]
    elif position == "back":
        string_to_return = string[len(string) // 2 if len(string) % 2 == 0 else ((len(string) // 2) + 1):]

    return string_to_return


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
