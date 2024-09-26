# -*- coding: utf-8 -*-
counts = 0
def count_occurrences(arr):
    # Use Counter to count occurrences of each number in the array
    #counts = Counter(arr)
    
    return counts


def split_string_by_length(s, length):
    """
    Split a string into substrings of a specific length.
    
    Args:
    - s (str): The input string to be split.
    - length (int): The desired length of each substring.
    
    Returns:
    - list: A list of substrings of the input string, each with the specified length.
    """
    # Initialize an empty list to store the substrings
    substrings = []
    
    # Iterate over the input string with a step of 'length'
    for i in range(0, len(s), length):
        # Append the substring of length 'length' to the list
        substrings.append(s[i:i+length])
    
    return substrings

def array_to_dict(arr):
    return {i: arr[i] for i in range(len(arr))}

def fibonacci_iterative(n):
    """
    Parameters
    ----------
    n : int
        number of iterations to do.

    Returns
    -------
    fib_sequence : array of ints
        the values in the fibonacci sequence for the given iterations.

    """
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def print_array_of_arrays_to_file(array_of_arrays, filename):
    with open(filename, 'w') as file:
        for array in array_of_arrays:
            file.write(' '.join(map(str, array)) + '\n')
            
def read_distances(outer_arr, values_dict, iterations):
    distances = []
    if iterations > 0:
        for i, val in values_dict.items():
            if len(values_dict) > (i+2):
                nex = values_dict[i+1]
                distances.append(nex - val)

        outer_arr.append(distances)
        return read_distances(outer_arr, array_to_dict(distances),iterations-1)
    else:
        return outer_arr


