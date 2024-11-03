class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value) -> None:
        if 0 <= value and value <= 100:
            obj.__dict__[self.name] = value
        else:
            raise ValueError("Price must be between 0 and 100.")


class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:        
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value) -> None:
        if obj.__dict__.get(self.name) is None: #only the first time
            obj.__dict__[self.name] = value
        else:
            raise ValueError(f"{self.name.capitalize()} can not be changed.")        


class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author, name, price) -> None:
        self.author = author
        self.name = name        
        self.price = price   


def test_price_control(b: Book, value):
    try:
        b.price = value
    except Exception as e:
        assert isinstance(e, ValueError)
        assert str(e) == "Price must be between 0 and 100."
    else:
        raise AssertionError("wrong")

def test_name_control(b: Book, value):
    try:
        b.name = value
    except Exception as e:
        assert isinstance(e, ValueError)
        assert str(e) == "Name can not be changed."
    else:
        raise AssertionError("wrong")

def test_author_control(b: Book, value):
    try:
        b.author = value
    except Exception as e:
        assert isinstance(e, ValueError)
        assert str(e) == "Author can not be changed."
    else:
        raise AssertionError("wrong")

def tests():
    b = Book("William Faulkner", "The Sound and the Fury", 12)
    assert f"Author='{b.author}', Name='{b.name}', Price='{b.price}'" == "Author='William Faulkner', Name='The Sound and the Fury', Price='12'"
    
    b.price = 55
    assert b.price == 55
    test_price_control(b, -12)
    test_price_control(b, 101)

    test_author_control(b, "new author")
    test_name_control(b, "new name")

if __name__ == "__main__":
    tests()
