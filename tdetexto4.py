#izabelli da rocha


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
    filename = 'teste4.txt'
    try:
        operations = read_input_file(filename)
        results = execute_operations(operations)
        print_results(results)
    except Exception as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
