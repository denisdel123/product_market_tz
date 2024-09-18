def generate_sequence(n):
    result = []
    number = 1

    while len(result) < n:
        result.extend([number] * number)
        number += 1

    return result[:n]


n = int(input("Введите количество элементов: "))
sequence = generate_sequence(n)
print("Последовательность:", sequence)
