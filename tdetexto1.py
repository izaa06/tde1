#izabelli da rocha
"""
O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
4
U
3, 5, 67, 7
1, 2, 3, 4
I
1, 2, 3, 4, 5
4, 5
D
1, A, C, 34
A, C, D, 23
C
3, 4, 5, 5, A, B, R
1, B, C, D, 1
Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e
{𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
a informação e a formatação mostrada a seguir:
União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}
Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e
pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.
"""


def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    num_operations = int(lines[0].strip())
    operations = []

    index = 1
    for _ in range(num_operations):
        operation_code = lines[index].strip()
        set1 = set(map(str.strip, lines[index + 1].strip().split(',')))
        set2 = set(map(str.strip, lines[index + 2].strip().split(',')))
        operations.append((operation_code, set1, set2))
        index += 3

    return operations


def execute_operations(operations):
    results = []

    for operation_code, set1, set2 in operations:
        if operation_code == 'U':
            result = set1.union(set2)
            operation_name = 'União'
        elif operation_code == 'I':
            result = set1.intersection(set2)
            operation_name = 'Interseção'
        elif operation_code == 'D':
            result = set1.difference(set2)
            operation_name = 'Diferença'
        elif operation_code == 'C':
            result = {(a, b) for a in set1 for b in set2}
            operation_name = 'Produto cartesiano'
        else:
            raise ValueError(f"Operação desconhecida: {operation_code}")

        results.append((operation_name, set1, set2, result))

    return results


def print_results(results):
    for operation_name, set1, set2, result in results:
        if operation_name == 'Produto cartesiano':
            # produto cartesiano, o resultado é uma lista de duplas
            result_str = ', '.join(f"({a}, {b})" for a, b in sorted(result))
        else:
            # os conjuntos são convertidos em listas e ordenados
            result_str = ', '.join(
                sorted(result, key=lambda x: (x.isdigit(), x)))

        set1_str = ', '.join(sorted(set1, key=lambda x: (x.isdigit(), x)))
        set2_str = ', '.join(sorted(set2, key=lambda x: (x.isdigit(), x)))

        # formatação do print
        print(
            f"{operation_name}: conjunto 1 {{{set1_str}}}, conjunto 2 {{{set2_str}}}. Resultado: {{{result_str}}}"
        )


def main():
    filename = 'teste.txt'
    try:
        operations = read_input_file(filename)
        results = execute_operations(operations)
        print_results(results)
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
