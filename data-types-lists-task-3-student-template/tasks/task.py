from typing import List

def mul(exclude_index: int, nums: List[int]) -> int:    
    result = 1
    for i in range(0, len(nums)): 
        if i != exclude_index:
            result *= nums[i]
    return result

def foo(nums: List[int]) -> List[int]:        
    return [mul(index, nums) for index in range(0, len(nums)) ]

def test_positive_cases():
    assert foo([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert foo([3, 2, 1]) == [2, 3, 6]
    assert foo([1, 2, 0, 3]) == [0, 0, 6, 0]
    assert foo([-1, -2, -3]) == [6, 3, 2]
    assert foo([-1, 2, -3, 4]) == [-24, 12, -8, 6]
   
def test_negative_cases():
    assert foo([1]) == [1]
    assert foo([]) == []
    
    
if __name__ == "__main__":    
    test_positive_cases()
    test_negative_cases()    