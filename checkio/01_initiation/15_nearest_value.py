def nearest_value(values: set, one: int) -> int:
    ''' 01 Initation: 15 Nearest Value
    Returns the value in values closest to one. If two values are equally close, it chooses the lowest of the two
    '''

    import numpy as np
    
    # First make dictionary mapping each value in the set to the distance from one
    distance = {}
    for num in values:
        distance[str(num)] = np.abs(one-num)
        
    # Returns the minimum number of these. The list comprehension picks out the key of lowest value,
    # and then the minimum value is picked out with the min()-function. Ensures that if there are more than
    # one key with the minimum value, that the lowest of the keys will be returned.
    return min([int(k) for k,v in distance.items() if v == min(distance.values())])
        
    


if __name__ == "__main__":
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({5}, 5) == 5
    assert nearest_value({5}, 7) == 5
    assert nearest_value({0, -2}, -1) == -2
    print("Coding complete? Click 'Check' to earn cool rewards!")