import os

class DirectoryControl:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:        
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value) -> None:
        if os.path.isdir(value): # dir exists
            obj.__dict__[self.name] = value
        else:
            raise ValueError(f"{self.name.capitalize()} '{value}' does not Exist")        


class Cd:
    new_path = DirectoryControl()

    def __init__(self, new_path):
        self.old_path = os.getcwd()
        self.new_path = new_path
        self.current_path = self.old_path

    def __enter__(self):                    
        self.current_path = self.new_path
        os.chdir(self.current_path)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        os.chdir(self.old_path)          
        self.current_path = self.old_path   

if __name__ == "__main__":
    with Cd("C:/Users/Joseph_Higaki/projects/magic-methods-task-6-student-template/toastee") as a:
        print(a.old_path)
        print(a.current_path)
