def get_longest_word(s: str) -> str:
    words = s.split()    
    longest_word = ''
    for w in words:
        if len(w) > len(longest_word):
            longest_word = w
    return longest_word


def test_positive_cases():
    assert get_longest_word('Python is simple and effective!') == 'effective!'
    assert get_longest_word('Lorem ipsum trate') == 'Lorem'
    assert get_longest_word('   ') == ''
    assert get_longest_word('   a d  d') == 'a'
    assert get_longest_word('24342 juhfssdfsuh fdhd erwe s\\nsdfs dsdgfs ff\\tfsdf') == 'juhfssdfsuh'
    assert get_longest_word('24342 jusuh fdhd erwe s\\nsdfs dsdgfs ff\\tfsdf') == 'ff\\tfsdf'
    assert get_longest_word('24342 juhfssdfsuh fdhd erwe s\\nsdfs dsdgfs fsdfdsfsdfsdfs32sdfsdfs ff\\tfsdf') == 'fsdfdsfsdfsdfs32sdfsdfs'    
    assert get_longest_word('24342 123456789 juhfssdf fdhd erwe 987654321 012345678') == '123456789'    
    assert get_longest_word('Python is simple\nand\teffective!')== 'effective!'
    assert get_longest_word('Python, AND dELPHI ARE simple\nand\teffective!')== 'effective!'

def test_negative_cases():
    assert get_longest_word('Python is simple and effective!') != 'simple'
    assert get_longest_word('Lorem ipsum trate') != 'traten'
    assert get_longest_word('24342 juhfssdf fdhd erwe s\\nsdfs dsdgfs ff\\tfsdf') != 'dsdgfs'
    assert get_longest_word('24342 jusuh fdhd erwe s\\nsdfs dsdgfs ff\\tfsdf') != 's\\nsdfs'
    assert get_longest_word('24342 juhfssdf fdhd erwe s\\nsdfs dsdgfs fsdfdsfsdfsdfs32sdfsdfs ff\\tfsdf') != '24342'    

if __name__ == "__main__":    
    test_positive_cases()
    test_negative_cases()
    print('success')