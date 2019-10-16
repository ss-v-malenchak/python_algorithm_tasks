"""
178.5
Даны натуральные числа n, A1, ..., An.
Определить количество членов Ak последовательности A1, ..., An
удовлетворящих условию 2^k < Ak < k!.
"""

import math


def get_count_of_elements_by_condition(sequence):
    """
    Count how many integer numbers satisfy the condition 2^k < Ak < k!.
    :param sequence: some sequence of integer number.
    :return: count of numbers.
    """
    elements_and_indexes = {sequence[i]: i + 1
                            for i in range(1, len(sequence) - 1)}
    filtered_values = filter(lambda element:
                             2 ** element[1] < element[0] < math.factorial(element[1]),
                             elements_and_indexes.items())
    return len(dict(filtered_values))


def task_178_5_menu():
    print('-' * 100)
    print(f'Function logic:\n{get_count_of_elements_by_condition.__doc__}')
    print('-' * 50)
    print("Input some number sequence of numbers by \' \':\n")
    try:
        sequence = [int(number) for number in input().split(' ')]
        print(f'Result: {get_count_of_elements_by_condition(sequence)}')
    except Exception as error:
        print(f'{error}. Try again!'.title())


if __name__ == '__main__':
    task_178_5_menu()