from contextlib import ContextDecorator
import datetime
import time


class LogFile(ContextDecorator):
    LOG_LINE_TEMPLATE = 'Start: {0} | Run: {1} | An error occurred: {2}\n'
    def __init__(self, file_name):
        self.start_time = datetime.datetime.now()
        self.file_name = file_name 

    def __enter__(self):
        self.log_file = open(self.file_name, "a")
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.end_time = datetime.datetime.now()
        run_time = self.end_time - self.start_time

        error_message = exc_value if exc_type else "None" 
        self.log_file.write(self.LOG_LINE_TEMPLATE.format(self.start_time, run_time, error_message))
        self.log_file.close()
        # returning False would make exception to be raised
        return not exc_type  #if exc_type: raise exc_type(exc_value).with_traceback(exc_tb) 
    
        

@LogFile('my_trace.log')
def logging_messages():
    print("before")    
    print("sleep 1")
    time.sleep(1)
    print("after")

@LogFile('my_trace.log')
def logging_div_zero():
    time.sleep(1)
    return 1/0


def func1(i: int):
    time.sleep(1)
    return 2 ** i

def test_logfile():
    #this is how the pipeline mechanism of the course tests it
    iter_number = 10
    test_func = LogFile("dfdsf")(func1)
    for i in range(iter_number):
        assert test_func(i) == 2 ** i


if __name__ == "__main__":
    logging_messages()    
    logging_div_zero()