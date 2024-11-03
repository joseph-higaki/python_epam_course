from collections import UserDict
from collections import deque


class HistoryDict(UserDict):
    def __init__(self, *args, **kwargs):        
        self.history = deque([], 5)
        super().__init__(*args, **kwargs)        

#    def __setitem__(self, key, value):
#        self.history.append(key)
#        super().__setitem__(key, value)

    def set_value(self, key, value):
        self.history.append(key)
        self[key] = value

    def get_history(self):
        return list(self.history)

def tests():
    d = HistoryDict({"foo": 42})
    d.set_value("bar", 43)
    assert d.get_history() == ["bar"]
    

if __name__ == "__main__":
    tests()