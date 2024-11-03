import functools

def decorator_apply(lambda_func):
    '''
    Add your implementation here
    '''    
    def decorator_wrapper(func):
        @functools.wraps(func)
        def wrapper(arg):
            result = func(arg)            
            return lambda_func(result)
        return wrapper
    return decorator_wrapper



@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num


print(return_user_id(32))