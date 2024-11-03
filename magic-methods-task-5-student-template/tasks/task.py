import os
import shutil
import uuid
#import pathlib

class TempDir:
    def __init__(self, start_path = None):
        self.old_path = start_path if start_path else os.getcwd()
        self.new_path = os.path.join(self.old_path, str(uuid.uuid4()))
        self.current_path = self.old_path 

    def __enter__(self):        
        os.mkdir(self.new_path)
        self.current_path = self.new_path
        os.chdir(self.current_path)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        os.chdir(self.old_path)
        shutil.rmtree(self.current_path)        
        self.current_path = self.old_path             

if __name__ == "__main__":
    with TempDir() as a:
        print(a.old_path)
        print(a.current_path)

