class Counter:
    def __init__(self, start:int = 0, stop:int = -1) -> None:
        self.current = self.start = start
        self.stop = stop

    def increment(self):
        if self.stop == -1 or self.current < self.stop:
            self.current += 1
    
    def get(self):
        return self.current

def tests():
    c = Counter(start=42)
    c.increment()
    assert c.get() == 43

    c = Counter()
    c.increment()
    assert c.get() == 1
    c.increment()
    assert c.get() == 2

    c = Counter(start=42, stop=43)
    c.increment()
    assert c.get() == 43
    c.increment()
    #Maximal value is reached.
    assert c.get() == 43

    

if __name__ == "__main__":
    tests()