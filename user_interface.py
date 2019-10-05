from task178_4 import get_elements_less_arithmetic_mean_of_its_neighbor
from task178_5 import get_elements_by_condition
from task555 import get_pascal_triangle


def input_sequence_of_numbers():
    """
    Convert string of numbers entered by user to list of numbers.
    :return: list of integer numbers.
    """
    print("Input some number sequence of numbers by \' \':")
    try:
        sequence = [int(number) for number in input().split(' ')]
    except Exception:
        print('Input error. Try again!')
        return []
    return sequence


def input_triangle_levels_count():
    """
    Get user's number.
    :return: number of triangle levels.
    """
    print('Input triangle levels count:')
    try:
        levels_count = int(input())
    except Exception:
        print('Input error. Try again!')
        return 0
    return levels_count


if __name__ == '__main__':
    tasks = {
        1: {
            'interface': input_sequence_of_numbers,
            'function': get_elements_less_arithmetic_mean_of_its_neighbor
        },
        2: {
            'interface': input_sequence_of_numbers,
            'function': get_elements_by_condition
        },
        3: {
            'interface': input_triangle_levels_count,
            'function': get_pascal_triangle
        }
    }

    while True:
        print("1 for task 178.4\n2 for task 178.5\n3 for task 555\nsmth else to exit")
        try:
            option = int(input())
            incoming_data = tasks[option]['interface']()
            result = tasks[option]['function'](incoming_data)
            print('Answer:', result, sep='\n')
        except Exception:
            break
