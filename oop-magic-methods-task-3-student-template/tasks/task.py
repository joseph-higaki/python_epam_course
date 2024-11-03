from __future__ import annotations
from typing import Type

class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """
    exchange_rates = {
                        'EUR': {
                            'EUR': 1.00,
                            'USD': 2.00,
                            'GBP': 100.00
                        },
                        'USD': {
                            'USD': 1.00,
                            'EUR': 0.50,        
                            'GBP': 50.00
                        },
                        'GBP': {
                            'GBP': 1.00,
                            'EUR': 0.01,        
                            'USD': 0.02
                        }    
                    }

    symbol = ""

    def __init__(self, value: float):
        self.value = value    
    
    @classmethod 
    def _get_exchange(cls, to_currency: str) -> float:
        rate = cls.exchange_rates[cls.symbol][to_currency]         
        if not rate:
            raise ValueError(f"Exchange rate {cls.symbol}-{to_currency} not found")
        return rate

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        return f"{cls._get_exchange(other_cls.symbol)} {other_cls.symbol} for 1 {cls.symbol}"
        

    def to_currency(self, other_cls: Type[Currency]):
        return other_cls(self.value * self.__class__._get_exchange(other_cls.symbol))
    
    def __str__(self) -> str:
        return f"{self.value} {self.__class__.symbol}"
    
    def __gt__(self, other: Currency) -> bool:
        return self.value > other.to_currency(self.__class__).value
    
    def __lt__(self, other: Currency) -> bool:
        return self.value < other.to_currency(self.__class__).value
    
    def __eq__(self, other: Currency) -> bool:
        return self.value == other.to_currency(self.__class__).value

    def __add__(self, other: Currency) -> Type[Currency]:
        return self.__class__(self.value + other.to_currency(self.__class__).value)      


class Euro(Currency):
    symbol = "EUR"


class Dollar(Currency):
    symbol = "USD"


class Pound(Currency):
    symbol = "GBP"



def test_course_list(statements: List[Tuple[Type[Currency], Type[Currency], str]]):
    for statement in statements:
        test_course(*statement)    

def test_course(from_cls: Type[Currency], to_cls: Type[Currency], result: str):
    assert from_cls.course(to_cls) == result


def test_to_currency_list(statements: List[Tuple[Type[Currency], float, Type[Currency], str]]):
    for statement in statements:
        test_to_currency(*statement)    

def test_to_currency(from_cls: Type[Currency], value:float, to_cls: Type[Currency], result: str) -> str:
    a = from_cls(value)
    b = a.to_currency(to_cls)
    assert isinstance(b, to_cls)
    assert str(b) == result


def tests():
    e = Euro(100)
    assert str(e) == "100 EUR"
    assert e.to_currency(Dollar).value == 200.0
    assert str(e.to_currency(Dollar)) == "200.0 USD"
    assert f"e.to_currency(Dollar) = {e.to_currency(Dollar)}" == "e.to_currency(Dollar) = 200.0 USD"
    
    assert e.to_currency(Pound).value == 10000.0
    assert str(e.to_currency(Pound)) == "10000.0 GBP"
    assert f"e.to_currency(Pound) = {e.to_currency(Pound)}" == "e.to_currency(Pound) = 10000.0 GBP"

    assert e.to_currency(Euro).value == 100.0
    assert str(e.to_currency(Euro)) == "100.0 EUR"
    assert f"e.to_currency(Euro) = {e.to_currency(Euro)}" == "e.to_currency(Euro) = 100.0 EUR"

    r = Pound(100)    
    assert str(r) == "100 GBP"
    assert r.to_currency(Dollar).value == 2.0
    assert str(r.to_currency(Dollar)) == "2.0 USD"
    assert f"r.to_currency(Dollar) = {r.to_currency(Dollar)}" == "r.to_currency(Dollar) = 2.0 USD"
    
    assert r.to_currency(Euro).value == 1.0
    assert str(r.to_currency(Euro)) == "1.0 EUR"
    assert f"r.to_currency(Euro) = {r.to_currency(Euro)}" == "r.to_currency(Euro) = 1.0 EUR"

    assert r.to_currency(Pound).value == 100.0
    assert str(r.to_currency(Pound)) == "100.0 GBP"
    assert f"r.to_currency(Pound) = {r.to_currency(Pound)}" == "r.to_currency(Pound) = 100.0 GBP"

    d = Dollar(200)
    assert (e + r).value ==  101.0
    assert str(e + r) == "101.0 EUR"
    assert f"e + r  =>  {e + r}" ==  "e + r  =>  101.0 EUR"
    
    assert (r + d).value ==  10100.0
    assert str(r + d) ==  "10100.0 GBP"
    assert f"r + d  =>  {r + d}" == "r + d  =>  10100.0 GBP"

    assert (d + e).value ==  400.0
    assert str(d + e) ==  "400.0 USD"
    assert f"d + e  =>  {d + e}" == "d + e  =>  400.0 USD"

    test_course_list([
            (Euro, Dollar, "2.0 USD for 1 EUR"),
            (Euro, Pound, "100.0 GBP for 1 EUR"),
            (Euro, Euro, "1.0 EUR for 1 EUR"),
            (Dollar, Euro, "0.5 EUR for 1 USD"),
            (Dollar, Pound, "50.0 GBP for 1 USD"),
            (Dollar, Dollar, "1.0 USD for 1 USD"),
            (Pound, Dollar, "0.02 USD for 1 GBP"),
            (Pound, Euro, "0.01 EUR for 1 GBP"),
            (Pound, Pound, "1.0 GBP for 1 GBP"),
            ])    

    test_to_currency_list( [
            (Euro, 100, Dollar, "200.0 USD"),
            (Euro, 20, Pound, "2000.0 GBP"),
            (Euro, 50, Euro, "50.0 EUR"),
            (Dollar, 90, Euro, "45.0 EUR"),
            (Dollar, 40, Pound, "2000.0 GBP"),
            (Dollar, 100, Dollar, "100.0 USD"),
            (Pound, 18, Dollar, "0.36 USD"),
            (Pound, 30, Euro, "0.3 EUR"),
            (Pound, 15, Pound, "15.0 GBP"),
            ])

if __name__ == "__main__":
    tests()