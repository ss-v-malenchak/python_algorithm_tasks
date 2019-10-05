def get_elements_less_arithmetic_mean_of_its_neighbor(sequence):
    """
    Count how many integer numbers satisfy the condition
    Ak < (Ak-1 + Ak+1 ) / 2.
    :param sequence: some sequence of integer number.
    :return: count of numbers.
    """
    arithmetic_means_for_elements = {sequence[i]:
                                     (sequence[i-1] + sequence[i+1]) / 2
                                     for i in range(1, len(sequence) - 1)}
    filtered_values = filter(lambda element: element[0] < element[1],
                             arithmetic_means_for_elements.items())
    return len(dict(filtered_values))
