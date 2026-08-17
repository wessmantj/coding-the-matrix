
def week_to_minutes(n: int) -> int:
    '''number of minutes in n weeks'''
    return n * 7 * 24 * 60

def remainder(dividend, divisor):
    '''find remainder without mod'''
    floor_div = dividend // divisor
    return dividend - (divisor * floor_div)

def is_sum_divisible(numbers: list[int], divisor: int) -> bool:
    '''tests whether sum of numbers is divisible by given number'''
    if divisor == 0:
        raise ValueError("Divisor can't be zero.")
    
    return sum(numbers) % divisor == 0

def square_elements(set):
    '''comprehension that squares elements in a set'''
    return {2**x for x in set}

def average(elements: list):
    '''expression whose value. is the average of the elements list'''
    n = len(elements)
    if n == 0:
        raise ValueError("list can't be empty.")
    return sum(elements) / n

def sum_of_elements(numbers: list[list[int]]) -> int:
    '''evaluates to the sum of all numbers in all the lists'''
    return sum(sum(sublist) for sublist in numbers)

def zero_sum_triples(values: set[int]) -> tuple[int, int, int]:
    '''given a set of values return tuple of 3 elements that sum to zero'''
    
    return [(i, j, k) for i in values for j in values for k in values if i + j + k == 0 and (i, j, k) != (0, 0, 0)][0]