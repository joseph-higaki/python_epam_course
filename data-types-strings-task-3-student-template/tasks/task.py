def replacer(s: str) -> str:
    result = ''
    for char in s:        
        replaced_char = char
        if char == r'"':
            replaced_char = r"'"
        elif char == r"'":
            replaced_char = r'"'
        result = result + replaced_char
    return result


def test_positive_cases():
    assert replacer(""" ada asd asd  asda " """) ==  (""" ada asd asd  asda ' """)
    assert replacer(""" ada asd asd  asda ' """) ==  (""" ada asd asd  asda " """)
    assert replacer(""" ada asd asd " asda ' """) ==  (""" ada asd asd ' asda " """)    

def test_negative_cases():
    True

if __name__ == "__main__":    
    test_positive_cases()
    test_negative_cases() 
    print('sucess')   