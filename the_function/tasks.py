
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

