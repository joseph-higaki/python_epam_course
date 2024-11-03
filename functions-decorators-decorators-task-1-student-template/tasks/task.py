from typing import Dict
import time 

execution_time: Dict[str, float] = {}

def time_decorator(func):
    """
    Create a decorator function `time_decorator`
    which has to calculate decorated function execution time
    and put this time value to `execution_time` dictionary where `key` is
    decorated function name and `value` is this function execution time.
    """
    def wrapper(a, b, sleep_time):
        start = time.time()
        result = func(a, b, sleep_time)
        end = time.time()        
        execution_time[func.__name__] = end-start
        return result
    return wrapper

@time_decorator 
def func_add(a, b, sleep_time):
    time.sleep(sleep_time)
    return a + b

print(func_add(10, 13, 0.02))
print(execution_time)

print(func_add(10, -1, 0.2))
print(execution_time)

print(func_add(6565, 13, 0.3))
print(execution_time)


