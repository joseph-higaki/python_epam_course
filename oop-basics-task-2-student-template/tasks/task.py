# Complete the following code according to the task in README.md.
# Don't change names of classes. Create names for the variables
# exactly the same as in the task.
from typing import List, Union


class SchoolMember:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def show(self) -> str:
        return f'Name: {self.name}, Age: {self.age }'


class Teacher(SchoolMember):
    def __init__(self, name: str, age: int, salary: int) -> None:
        super().__init__(name, age)
        self.salary = salary

    def show(self) -> str:
        return super().show() + f', Salary: {self.salary}'


class Student(SchoolMember):
    def __init__(self, name: str, age: int, grades: Union[int | List[int] | dict[str, int]]) -> None:
        super().__init__(name, age)
        self.grades = grades

    def print_grades(self):
        if isinstance(self.grades, int):
            return self.grades
        elif isinstance(self.grades, List) or isinstance(self.grades, dict):
            return str(self.grades)       


    def show(self) -> str:
        return super().show() + f', Grades: {self.print_grades()}'

def tests():
    persons = [Teacher("Mr.Snape", 40, 3000), Student("Harry", 16, 75)]
    assert persons[0].show() == "Name: Mr.Snape, Age: 40, Salary: 3000"
    assert persons[1].show() == "Name: Harry, Age: 16, Grades: 75"
    assert Teacher("James Smith", 40, 1000).show() == "Name: James Smith, Age: 40, Salary: 1000"
    assert Teacher("Mr.Robot", 30, 0).show() == "Name: Mr.Robot, Age: 30, Salary: 0"
    assert Teacher("Ph.D.Cooper", 34, 10).show() == "Name: Ph.D.Cooper, Age: 34, Salary: 10"
    assert Student("Henry", 14, [5, 3, 5, 2, 3, 4, 5]).show() == "Name: Henry, Age: 14, Grades: [5, 3, 5, 2, 3, 4, 5]" 
    assert Student("Penny", 17, {"Math": 5, "PE": 3}).show() == "Name: Penny, Age: 17, Grades: {'Math': 5, 'PE': 3}"


if __name__ == "__main__":  
    tests()