

def union(*args) -> set:    
    return set([item for arg in args for item in arg ])
               
def intersect(*args) -> set:
    result = ()
    size = len(args)
    if size > 0:
        result = [item for item in args[0]]
        i = 0
        while i < size:
            result = [item for item in args[i] if item in result]
            i += 1        
    return set(result)

def test_union():
    assert union(('S', 'A', 'M'), ['S', 'P', 'A', 'C']) == {'S', 'P', 'A', 'M', 'C'}

def test_intersect():
    assert intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C')) == {'S', 'C'}

if __name__ == "__main__":    
    test_union()
    test_intersect()