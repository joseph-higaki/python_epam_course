from abc import ABC
from abc import abstractmethod

MIN_PURCHASE_PRICE = 100000.0

class Vehicle(ABC):
    def __init__(
            self,
            brand_name: str,
            year_of_issue: int,
            base_price: int,
            mileage: int
    ):
        self.brand_name = brand_name 
        self.year_of_issue = year_of_issue 
        self.base_price = base_price 
        self.mileage = mileage         
    
    @abstractmethod
    def wheels_num(self) -> int:
        raise NotImplementedError("You have to implement wheels_num() method") 

    @staticmethod
    def format_vehicle_type(brand: str, type: str) -> str:
        return f'{brand} {type}'

    def vehicle_type(self) -> str:
        return self.format_vehicle_type(self.brand_name, self.__class__.__name__)
    
    def is_motorcycle(self) -> bool:
        return self.wheels_num() == 2

    @property
    def purchase_price(self) -> float:
        result = self.base_price - 0.1 * self.mileage
        return MIN_PURCHASE_PRICE if result < MIN_PURCHASE_PRICE else result
    
    @property
    def description(self) -> list[str]:
        result = []
        result.append(f"Vehicle type={self.vehicle_type()}")
        result.append(f"Is motorcycle={self.is_motorcycle()}")
        result.append(f"Purchase price={self.purchase_price}")
        return result

# Don't change class implementation
class Car(Vehicle):
    def wheels_num(self):
        return 4


# Don't change class implementation
class Motorcycle(Vehicle):    
    def wheels_num(self):
        return 2


# Don't change class implementation
class Truck(Vehicle):
    def wheels_num(self):
        return 10


# Don't change class implementation
class Bus(Vehicle):
    def wheels_num(self):
        return 6

def tests():
    assert Car(brand_name="Toyota", year_of_issue=2020, base_price=1_000_000, mileage=150_000).description == ["Vehicle type=Toyota Car", "Is motorcycle=False", "Purchase price=985000.0"]    
    assert Motorcycle(brand_name="Suzuki", year_of_issue=2015, base_price=800_000, mileage=35_000).description == ["Vehicle type=Suzuki Motorcycle", "Is motorcycle=True", "Purchase price=796500.0"]
    assert Truck(brand_name="Scania", year_of_issue=2018, base_price=15_000_000, mileage=850_000).description == ["Vehicle type=Scania Truck", "Is motorcycle=False", "Purchase price=14915000.0"]
    assert Bus(brand_name="MAN", year_of_issue=2000, base_price=10_000_000, mileage=950_000).description == ["Vehicle type=MAN Bus", "Is motorcycle=False", "Purchase price=9905000.0"]

if __name__ == "__main__":
    tests()