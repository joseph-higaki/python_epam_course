from typing import Tuple
import math 

def get_tuple(num: int) -> Tuple[int]:        
    return tuple([int(n) for n in str(num)])

def test_positive_cases():
    assert get_tuple(87178291199) == (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
    assert get_tuple(1234567890) == (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
    assert get_tuple(0) == (0,)
    assert get_tuple(5) == (5,)
    assert get_tuple(9876543210) == (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
  
def test_negative_cases():
    assert get_tuple(1234567890) != (1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert get_tuple(0) != (0, 0)
    assert get_tuple(5) != (5, 5)
    assert get_tuple(9876543210) != (9, 8, 7, 6, 5, 4, 3, 2, 1)
    
    
if __name__ == "__main__":    
    test_positive_cases()
    test_negative_cases()    