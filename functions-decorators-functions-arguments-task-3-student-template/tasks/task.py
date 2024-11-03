from typing import Dict

def combine_dicts(*args:Dict[str, int]) -> Dict[str, int]:
    result = {}
    for dictionary in args:
        for key,value in dictionary.items():
            result[key] = result.get(key, 0) + value          
    return result

def test_combine_dicts():
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}

    assert combine_dicts(dict_1, dict_2) ==  {'a': 300, 'b': 200, 'c': 300}
    assert combine_dicts(dict_1, dict_2, dict_3) == {'a': 600, 'b': 200, 'c': 300, 'd': 100}



if __name__ == "__main__":    
    test_combine_dicts()    