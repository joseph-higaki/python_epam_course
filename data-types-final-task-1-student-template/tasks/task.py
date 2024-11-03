from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:        
    
    result = set([dict_value for dictionary in lst for dict_value in dictionary.values()])
    return result


def test_positive_cases():
    assert check([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]) == {'S005', 'S002', 'S007', 'S001', 'S009'}    
    assert check([{"A":"X001"}, {"B": "X002"}, {"C": "X001"}, {"D": "X003"}, {"E":"X003"}, {"F":"X004"},{"G":"X005"}]) == {'X001', 'X002', 'X003', 'X004', 'X005'}
    assert check([{"1":"T001"}, {"2": "T002"}, {"3": "T001"}, {"4": "T003"}, {"5":"T003"}, {"6":"T004"},{"7":"T005"}]) == {'T001', 'T002', 'T003', 'T004', 'T005'}
    assert check([{"key":"value"}, {"another_key": "value"}, {"yet_another_key": "another_value"}]) == {'value', 'another_value'}
    assert check([{}, {}]) == set()

def test_negative_cases():
    assert check([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]) != {'S005', 'S002', 'S001', 'S009'}
    assert check([{"A":"X001"}, {"B": "X002"}, {"C": "X001"}, {"D": "X003"}, {"E":"X003"}, {"F":"X004"},{"G":"X005"}]) != {'X001', 'X002', 'X003', 'X004'}
    assert check([{"1":"T001"}, {"2": "T002"}, {"3": "T001"}, {"4": "T003"}, {"5":"T003"}, {"6":"T004"},{"7":"T005"}]) != {'T001', 'T002', 'T003', 'T004'}
    assert check([{"key":"value"}, {"another_key": "value"}, {"yet_another_key": "another_value"}]) != {'value'}
    assert check([{}, {}]) != {}

if __name__ == "__main__":    
    test_positive_cases()
    test_negative_cases()    
