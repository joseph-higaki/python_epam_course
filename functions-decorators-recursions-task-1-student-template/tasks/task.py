from typing import List, Tuple, Union
from functools import reduce

def better_seq_sum(sequence: Union[List, Tuple]) -> int:
    result = 0
    for item in sequence: 
        if isinstance(item, int):
            result += item
        else:
            result += better_seq_sum(item)
    return result

def seq_sum(sequence: Union[List, Tuple]) -> int:
    if not sequence:
        result = 0
    elif isinstance(sequence[0], int):
        result = sequence[0] + seq_sum(sequence[1:])        
    else:
        result = seq_sum(sequence[0]) + seq_sum(sequence[1:])        
    return result
     
def test_seq_sum_func(func):
    sequence = [1,2,3,[4,5, (6,7)]]
    result = func(sequence)
    print(result)
    assert result == 28
    assert func([1, 2, 3, [4, 5, (6, 7)]]) == 28
    assert func([1, 2, [3, 4, [5, 6, [7, 8]]]]) == 36
    assert func([1, (2, 3), [[4, 5], 6]]) == 21
    assert func([]) == 0
    assert func([1, 2, 3]) == 6

if __name__ == "__main__":    
    test_seq_sum_func(seq_sum)  
    test_seq_sum_func(better_seq_sum)  
    