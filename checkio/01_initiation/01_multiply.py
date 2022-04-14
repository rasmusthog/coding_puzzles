def mult_two(a, b):
    ''' An intentionally silly implementation'''
    min_num = a if a <= b else b
    max_num = a if a >= b else b
    
    prod = 0
    for _ in range(min_num):
        prod += max_num
        
    return prod


def mult_two_copilot(a,b):
    '''
    This function should return product of a and b
    '''
    return a * b
    

if __name__ == "__main__":
    print("Example:")
    print(mult_two(3, 2))
    print(mult_two(10,10))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert mult_two(3, 2) == 6
    assert mult_two(1, 0) == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")