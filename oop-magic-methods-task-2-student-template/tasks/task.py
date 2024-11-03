class Bird:
    def __init__(self, name) -> None:
        self.name = name

    def _do(self, action) -> str:
        return f"{self.name} bird can {action}"

    def walk(self) -> str:
        return self._do("walk")    
    
    def __str__(self) -> str:
        return self.walk()

class EatingBird(Bird):
    def __init__(self, name, ration) -> None:
        super().__init__(name)
        self.ration = ration

    def eat(self) -> str:
        return f"It eats mostly {self.ration}"    
    
class FlyingBird(EatingBird):
    def __init__(self, name, ration = "grains") -> None:
        super().__init__(name, ration)        

    def fly(self) -> str:
        return self._do("fly")    
    
    def __str__(self) -> str:
        return f"{self.name} bird can walk and fly"


class NonFlyingBird(EatingBird):
    def __init__(self, name, ration = "fish") -> None:
        super().__init__(name, ration)
        self.ration = ration

    def fly(self) -> str:
        raise AttributeError(f"'{self.name}' object has no attribute 'fly'")

    def swim(self) -> str:
        return self._do("swim")

    def __str__(self) -> str:
        return f"{self.name} bird can walk and swim"


class SuperBird(NonFlyingBird, FlyingBird):
    def __str__(self) -> str:
        return f"{self.name} bird can walk, swim and fly"


def tests():
    b = Bird("Any")
    assert b.walk() == "Any bird can walk"

    p = NonFlyingBird("Penguin", "fish")
    assert p.swim() == "Penguin bird can swim"
    try:
        p.fly()
    except Exception as e:
        assert str(e) == "'Penguin' object has no attribute 'fly'"
    assert p.eat() == "It eats mostly fish"

    c = FlyingBird("Canary")
    assert str(c) == "Canary bird can walk and fly"
    assert c.eat() == "It eats mostly grains"
    
    s = SuperBird("Gull")
    assert str(s) == "Gull bird can walk, swim and fly"
    assert s.eat() == "It eats mostly fish"
    print(s.__class__.__mro__)


if __name__ == "__main__":
    tests()
    
