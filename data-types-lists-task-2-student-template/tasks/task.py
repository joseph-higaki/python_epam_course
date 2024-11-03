from typing import Union, List

ListType = List[Union[int, str]]

def get_fizzbuzz(item: int) -> Union[int, str]:    
    str_result = ''
    if item % 3 == 0 or item % 5 == 0:
        if item % 3 == 0:
            str_result += 'Fizz'
        if item % 5 == 0:
            str_result += 'Buzz'
        return str_result
    else:
        return item
                                

def get_fizzbuzz_list(n: int) -> ListType:
    return [get_fizzbuzz(item) for item in range(1, n + 1)]

def test_positive_cases():
    assert get_fizzbuzz_list(1) == [1]
    assert get_fizzbuzz_list(3) == [1, 2, 'Fizz']
    assert get_fizzbuzz_list(5) == [1, 2, 'Fizz', 4, 'Buzz']
    assert get_fizzbuzz_list(15) == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
    assert get_fizzbuzz_list(0) == []

def test_negative_cases():
    assert get_fizzbuzz_list(1) != []
    assert get_fizzbuzz_list(100) != []

    
if __name__ == "__main__":
    test_positive_cases()
    test_negative_cases()    