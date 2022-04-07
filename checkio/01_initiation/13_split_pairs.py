def split_pairs(a):
    
    pairs = []
    for i, letter in enumerate(a):
        if i%2 == 0 and i < len(a)-1:
            pairs.append(letter+a[i+1])
        elif i%2 == 0:
            pairs.append(letter+'_')

    return pairs


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")