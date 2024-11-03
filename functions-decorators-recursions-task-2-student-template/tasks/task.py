from typing import Any, List
from collections.abc import Iterable


def linear_seq(sequence: List[Any]) -> List[Any]:
    """
    Add your code here or call it from here   
    """
    result = []
    for item in sequence:
        if not isinstance(item, Iterable):
            result.append(item) 
        else:
            result += linear_seq(item)
    print(result)
    return result

def tests():
    assert linear_seq([1,2,3,[4,5, (6,7)]]) == [1,2,3,4,5,6,7]
    assert linear_seq([1, 2, [3, 4, [5, 6, [7, 8]]]]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert linear_seq([1, (2, 3), [[4, 5], 6]]) == [1, 2, 3, 4, 5, 6]
    assert linear_seq([]) == []
    assert linear_seq([1, 2, 3]) == [1, 2, 3]


if __name__ == "__main__":    
    tests()