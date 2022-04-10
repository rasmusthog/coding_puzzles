def checkio(words: str) -> bool:
    ''' A function that returns True if a string of words contain three words
    in a row (without being interrupted by a number). 
    
    '''


    consecutive_words = 0
    for word in words.split():
        consecutive_words = consecutive_words + 1 if word.isalpha() else 0

        # Return if the count reaches 3
        if consecutive_words == 3:
            return True
        
    return False



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
