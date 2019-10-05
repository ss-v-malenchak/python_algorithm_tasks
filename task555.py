def format_pascal_triangle(triangle):
    """
    Convert matrix of values to string.
    :param triangle: matrix of values.
    :return: string of values.
    """
    triangle_without_zeros = [list(filter(lambda element: element, row))
                              for row in triangle]
    return '\n'.join([' '.join(map(str, row))
                      for row in triangle_without_zeros])


def get_pascal_triangle(levels_count):
    """
    Count all values of pascal triangle and output formatted one.
    :param levels_count: count of levels of pascal triangle.
    :return: formatted string of values.
    """
    triangle = [[1] + [0]*(levels_count - 1)]
    for i in range(1, levels_count):
        triangle.append([1] + [triangle[i-1][j-1] + triangle[i-1][j]
                               for j in range(1, levels_count)])
    return format_pascal_triangle(triangle)
