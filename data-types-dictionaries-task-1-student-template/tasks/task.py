from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    # TODO: Add your code here
    s = s.lower()
    tuple_str = tuple(sorted(s))
    result = dict( [(char, s.count(char)) for char in tuple_str] )
    return result


def test_positive_cases():
    assert get_dict('Oh, it is python') == {" ": 3, ",": 1, "h": 2, "i": 2, "n": 1, "o": 2, "p": 1, "s": 1, "t": 2, "y": 1}
    assert get_dict('Hello, World!') == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}
    assert get_dict('A quick brown fox jumps over the lazy dog') == {'a': 2, ' ': 8, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'e': 2, 't': 1, 'h': 1, 'l': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}

def test_negative_cases():
    assert get_dict('Good Morning') != {'g': 2, 'o': 2, 'd': 1, ' ': 1, 'm': 1, 'r': 1, 'n': 1, 'i': 1}
    assert get_dict('Python') != {'p': 1, 'y': 1, 't': 1, 'h': 1, 'n': 1}
    assert get_dict('Testing') != {'t': 1, 'e': 1, 's': 1, 'i': 1, 'n': 1, 'g': 1}
  
if __name__ == "__main__":    
    test_positive_cases()
    test_negative_cases()    