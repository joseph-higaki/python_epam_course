from typing import Union
import math

NumType = Union[int, float]

def some_expression_with_rounding(a: NumType, b: NumType) -> NumType:
  result = None
  # add your code here
  result = (12 * a + 25 * b) / (1 + a**(2**b))	
  result = round(result, 2)  
  return result


def test_positive_cases():
    assert some_expression_with_rounding(2.0, 3.0) == 0.39
    assert some_expression_with_rounding(4.0, 5.0) == 0.00
    assert some_expression_with_rounding(1.0, 2.0) == 31.0
    assert some_expression_with_rounding(3.0, 4.0) == 0.00

def test_negative_cases():
    assert some_expression_with_rounding(2.0, 3.0) != 0.40
    assert some_expression_with_rounding(4.0, 5.0) != 0.01
    assert some_expression_with_rounding(1.0, 2.0) != 37.01
    assert some_expression_with_rounding(3.0, 4.0) != 0.28

    
if __name__ == "__main__":
    test_positive_cases()
    test_negative_cases()