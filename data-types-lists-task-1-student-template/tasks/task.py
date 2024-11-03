from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    # TODO: Add your code here
    my_list = list(str_list)
    a =  [item for item in my_list if my_list.count(item) == 1 ].sort()        
    new_list = []
    for item in str_list:
        if new_list.count(item) == 0:
            new_list.append(item)
    new_list.sort()
    return new_list

def test_positive_cases():
    assert sort_unique_elements(('red', 'white', 'black', 'red', 'green', 'black')) == ['black', 'green', 'red', 'white']
    

def test_negative_cases():
    assert sort_unique_elements(('red', 'white', 'black', 'red', 'green', 'black')) != ['green', 'red', 'white']
    assert sort_unique_elements(('red', 'white', 'black', 'red', 'green', 'black')) != ['green', 'red', 'black']

    
if __name__ == "__main__":
    test_positive_cases()
    test_negative_cases()    