from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values
    def __add__(self, b: str):
        return [f'{item} {b}' for item in self.values]



def tests():
    c = Counter([1, 2, 3]) + "mississippi"
    assert c == ["1 mississippi", "2 mississippi" , "3 mississippi"]

if __name__ == "__main__":
    tests()
