from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:    
    return { i: i**2 for i in range(1, num+1)}

def test_positive_cases():
    assert generate_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    assert generate_squares(3) == {1: 1, 2: 4, 3: 9}
    assert generate_squares(1) == {1: 1}
    assert generate_squares(0) == {}

def test_negative_cases():
    assert generate_squares(5) != {1: 2, 2: 5, 3: 10, 4: 17, 5: 26}
    assert generate_squares(3) != {1: 2, 2: 5, 3: 10}
    assert generate_squares(1) != {1: 2}
    assert generate_squares(0) != {1: 1}

if __name__ == "__main__":    
    test_positive_cases()
    test_negative_cases()    
    