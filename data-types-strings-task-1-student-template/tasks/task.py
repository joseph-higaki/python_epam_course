class Fraction:
    def __init__(self, numerator, denominator):
        if isinstance(numerator, int) and isinstance(denominator, int):
            self.numerator = numerator
            self.denominator = denominator

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator == other.numerator and self.denominator == other.denominator
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


def get_fraction(fraction: str) -> Fraction:
    result = None    
    numerator, denominator = map(int, fraction.split('/'))
    if isinstance(numerator, int) and isinstance(denominator, int) and denominator > 0:
        result = Fraction(numerator, denominator)
    return result

def validate_denominators(a: Fraction, b: Fraction) -> bool:
    return a.denominator == b.denominator

def get_fractions(a_b: str, c_b: str) -> str:    
    result = None
    a = get_fraction(a_b)
    b = get_fraction(c_b)
    if (a is not None) and (b is not None) and validate_denominators(a, b): 
        result = f'{a.numerator}/{a.denominator} + {b.numerator}/{b.denominator} = {a.numerator + b.numerator}/{b.denominator}'
    return result

def test_validate_denominators():
    assert validate_denominators(Fraction(1,3), Fraction(5,3)) == True
    assert validate_denominators(Fraction(1,7), Fraction(5,7)) == True
    assert validate_denominators(Fraction(4,9), Fraction(5,9)) == True
    assert validate_denominators(Fraction(1,3), Fraction(5,8)) == False
    assert validate_denominators(Fraction(9,10), Fraction(5,8)) == False

def test_validate_fraction():
    assert get_fraction('2/4') == Fraction(2,4)    
    assert get_fraction('0/9') == Fraction(0,9)    
    assert get_fraction('6/3') == Fraction(6,3)
    assert get_fraction('8/9') == Fraction(8,9)
    assert get_fraction('8/-9') == None
    assert get_fraction('8/0') == None

def test_positive_cases():
    assert get_fractions('1/3', '5/3') == '1/3 + 5/3 = 6/3'
    assert get_fractions('10/5', '3/5') == '10/5 + 3/5 = 13/5'
    assert get_fractions('3/7', '4/7') == '3/7 + 4/7 = 7/7'
    assert get_fractions('0/9', '1/9') == '0/9 + 1/9 = 1/9'
    assert get_fractions('6/4', '2/4') == '6/4 + 2/4 = 8/4'

def test_negative_cases():
    assert get_fractions('1/3', '5/3') != '1/3 + 5/3 = 7/3'
    assert get_fractions('2/5', '3/5') != '2/5 + 3/5 = 6/5'
    assert get_fractions('3/7', '4/7') != '3/7 + 4/7 = 8/7'
    assert get_fractions('0/9', '1/9') != '0/9 + 1/9 = 2/9'
    assert get_fractions('6/4', '2/4') != '6/4 + 2/4 = 19/4'

    
if __name__ == "__main__":
    test_validate_fraction()
    test_validate_denominators()
    test_positive_cases()
    test_negative_cases()    