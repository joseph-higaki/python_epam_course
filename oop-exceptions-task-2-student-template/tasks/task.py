from typing import Union

EXCEPTION_MASK = "Error code: "

def divide(str_with_ints: str) -> Union[float, str]:
    """
    Returns the result of dividing two numbers or an error message.
    :arg
        str_with_ints: str, ex. "4 2";
    :return
        result of dividing: float, ex. 2.0 (4 / 2 = 2.0);
        error response in "Error code: {error message}: str;
    """
    numbers = str_with_ints.split(" ", 1)
    try:
        numerator = int(numbers[0].strip())
        denominator = int(numbers[1].strip())        
    except ValueError as e:
        return f"{EXCEPTION_MASK}{str(e)}"
    try:    
        result = numerator / denominator
    except ZeroDivisionError as e:
        return f"{EXCEPTION_MASK}{str(e)}"
    return result

def test_exception(str_with_ints, exception_message):
    try:
        divide(str_with_ints)
    except Exception as e:
        assert str(e) == exception_message

ZERO_DIVISION_ERROR_CODE = "Error code: division by zero" 
INVALID_LITERAL = "Error code: invalid literal for int() with base 10: '{0}'"

def tests():
    assert divide("4 2") == 2.0    
    assert divide("5 5") == 1.0
    assert divide("7 2") == 3.5
    assert divide("4 0") == ZERO_DIVISION_ERROR_CODE
    assert divide("* 1") == INVALID_LITERAL.format("*")
    assert divide("1 0") == ZERO_DIVISION_ERROR_CODE
    assert divide("$ 1") == INVALID_LITERAL.format("$")
    assert divide("4 *") == INVALID_LITERAL.format("*")
    assert divide("% &") == INVALID_LITERAL.format("%")

#    test_exception("4 0", ZERO_DIVISION_ERROR_CODE)
 #   test_exception("* 1", INVALID_LITERAL.format("*"))
  #  test_exception("1 0", ZERO_DIVISION_ERROR_CODE)
   # test_exception("$ 1", INVALID_LITERAL.format("$"))
    #test_exception("4 *", INVALID_LITERAL.format("*"))
    #test_exception("% &", INVALID_LITERAL.format("%"))

if __name__ == "__main__":
    tests()