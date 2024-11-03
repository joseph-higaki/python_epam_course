from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    # TODO: Add your code here    
    return [(lst[index], lst[index + 1]) for index in range(0, len(lst) -1)]



def test_positive_cases():
    assert get_pairs([1, 2, 3, 8, 9]) == [(1, 2), (2, 3), (3, 8), (8, 9)]    
    assert get_pairs(['need', 'to', 'sleep', 'more']) == [('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]    
    assert get_pairs([1]) == []
    assert get_pairs([]) == []
    assert get_pairs([2, 2]) == [(2, 2)]
    assert get_pairs(['hi', 'hello', 'hey']) == [('hi', 'hello'), ('hello', 'hey')]
    assert get_pairs([1, 1, 1, 1]) == [(1, 1), (1, 1), (1, 1)]
    assert get_pairs(['x', 'y', 'z', 'a', 'b', 'c']) == [('x', 'y'), ('y', 'z'), ('z', 'a'), ('a', 'b'), ('b', 'c')]   
  
def test_negative_cases():
    assert get_pairs([-1, -2, -3, -4]) == [(-1, -2), (-2, -3), (-3, -4)]
    assert get_pairs([1, -2, 3, -4]) == [(1, -2), (-2, 3), (3, -4)]
    assert get_pairs([2, 2]) != [(2, 3)]
    assert get_pairs(['hi', 'hello', 'hey']) != [('hi', 'hey'), ('hello', 'hi')]
    assert get_pairs([1, 1, 1, 1]) != [(1, 2), (2, 1), (1, 2)]
    assert get_pairs(['x', 'y', 'z', 'a', 'b', 'c']) != [('x', 'a'), ('y', 'b'), ('z', 'c'), ('a', 'x'), ('b', 'y')]
   
if __name__ == "__main__":    
    test_positive_cases()
    #test_negative_cases()     