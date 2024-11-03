import functools

def validate(func):
  @functools.wraps(func)
  def wrapper(*args:int) -> str:
    
    if all([0 <= arg <= 256 for arg in args]):
      result = func(*args)  
    else:
      result = "Function call is not valid!"
    return result
  return wrapper

@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"

print(set_pixel(0, 127, 300))
print(set_pixel(0,127,250))