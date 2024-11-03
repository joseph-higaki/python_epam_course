def check_str(s: str) -> bool: 
    """
    Add your code here
    """
    result = True
    index_forward = 0
    index_reverse = len(s)-1
    while index_forward < index_reverse:
        while index_forward < index_reverse and not s[index_forward].isalnum():
            index_forward += 1
        while index_forward < index_reverse and not s[index_reverse].isalnum():
            index_reverse -= 1

        if s[index_forward].lower() != s[index_reverse].lower():
            result = False        
            break
        index_forward += 1
        index_reverse -= 1
    return result

def test_positive_cases():
    assert check_str("madam") == True
    assert check_str("racecar") == True
    assert check_str("level") == True
    assert check_str("noon") == True
    assert check_str("deed") == True
    assert check_str("redder") == True    
    assert check_str("No 'x' in Nixon") == True    
    assert check_str("A man, a plan, a canal - Panama") == True    

def test_negative_cases():
    assert check_str("reddefsdfr") != True
    assert check_str("sdfreddefsdfr") != True
    assert check_str("astroboy") != True

if __name__ == "__main__":    
    test_positive_cases()
    test_negative_cases() 
    print('sucess')   
