import time
import inspect

def write_log(log_line):
    # Append-adds at last
    with open("log.txt", "a") as f:
        f.write(f'{log_line}\n')

def log(fn):
    """
    Add your code here or call it from here   
    """
    #def wrapper(*args, **kwargs):        
    def wrapper(*args, **kwargs):        
        start = time.time()                       
        result =  fn(*args, **kwargs)
        end = time.time()

        # get argument names from inspect. This is an ordered collection
        param_values_list = [param.name for param in inspect.signature(fn).parameters.values()]
        # get argument name/ value. Same order 
        arg_dict = {param_values_list[i]:arg for i, arg in enumerate(args)}
        args_text = ', '.join( [f'{k}={v}' for k, v in arg_dict.items()] )
        kwargs_text = ', '.join( [f'{k}={v}' for k, v in kwargs.items()] )        

        write_log(f'{fn.__name__}; args: {args_text}; kwargs: {kwargs_text}; execution time: {(end-start):0.2f} sec.')        
        return result
    return wrapper

@log
def foo(a, b, **kwargs):    
    pass

foo(1, 2, c=3)


@log
def foo2(a, **kwargs):    
    pass

foo2(5, c=13)

@log
def foo3(**kwargs):    
    pass
foo3(c=13, g=54)
