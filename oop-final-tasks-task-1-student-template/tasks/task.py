from typing import Type


class Sun:    
    __instance = None
    @classmethod
    def inst(cls: Type):
        if not cls.__instance:
            cls.__instance = cls()
        return cls.__instance
    
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Sun, cls).__new__(cls, *args, **kwargs)
        return cls.__instance


if __name__ == "__main__":
    p = Sun.inst()
    f = Sun.inst()
    assert p is f
    t = Sun()
    assert t is f

