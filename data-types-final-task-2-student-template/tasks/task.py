from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    row_headers = range(row_start, row_end + 1)
    col_headers = range(column_start, column_end + 1)    
    result = [ [ row * col for col in col_headers ] for row in row_headers ]    
    return result
    
def test_positive_cases():
    assert check(2, 4, 3, 7) == [[6, 8, 10, 12, 14], [9, 12, 15, 18, 21], [12, 16, 20, 24, 28]]
    assert check(1, 3, 1, 3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    assert check(5, 6, 5, 6) == [[25, 30], [30, 36]]
    assert check(1, 1, 1, 1) == [[1]]
    assert check(3, 3, 3, 3) == [[9]]


def test_negative_cases():
    assert check(2, 4, 3, 7) != [[6, 8, 10, 12], [9, 12, 15, 18], [12, 16, 20, 24]]
    assert check(1, 3, 1, 3) != [[1, 2], [2, 4], [3, 6]]
    assert check(5, 6, 5, 6) != [[25], [30]]
    assert check(1, 1, 1, 1) != [[2]]
    assert check(3, 3, 3, 3) != [[8]]

if __name__ == "__main__":    
    test_positive_cases()
    test_negative_cases()    
    