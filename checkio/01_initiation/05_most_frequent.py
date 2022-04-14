def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    
    freq = {}
    for string in data:
        if not string in freq:
            freq[string] = 1

        else:
            freq[string] = freq[string] + 1

    max_ = 0
    max_item = None

    for key, val in freq.items():
        if val > max_:
            max_ = val 
            max_item = key

    return max_item


def most_frequent_copilot(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    return max(set(data), key=data.count)


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")
