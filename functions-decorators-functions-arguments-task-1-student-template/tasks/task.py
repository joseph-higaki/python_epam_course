from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    for filter in filters:
        data = filter(data)
    return selector(data)  


def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""
    def do_select(data: DataType) -> DataType:
        return [{k: v for k, v in row_dict.items() if k in columns  } for row_dict in data]         
    return do_select


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""
    def do_filter(data: DataType) -> DataType:
        return [row_dict for row_dict in data if row_dict[column] in values]    
    return do_filter

def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
        {'name': 'Emily', 'gender': 'female', 'sport': 'volleyball'}
    ]
    value = query(
        friends,
        select('name', 'gender', 'sport'),
        field_filter('sport', 'Basketball', 'volleyball'),
        field_filter('gender', 'male'),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value

    value = query(
        friends,
        select(*('name', 'gender')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',)))
    )
    assert [{'gender': 'male', 'name': 'Sam'}] == value    

    value = query(
        friends,
        select('name'),
        field_filter(*('sport', *('Basketball', 'volleyball')))
    )
    assert [{'name': 'Sam'}, {'name': 'Emily'}] == value        

    value = query(
        friends,
        select('name'),
        field_filter(*('sport', 'volleyball'))
    )
    assert [{'name': 'Emily'}] == value    

    value = query(
        friends,
        select(*('name','gender')),
        field_filter('sport', 'volleyball')
    )
    assert [ {'name': 'Emily', 'gender': 'female'}] == value    

    value = query(
        friends,
        select(*('name','gender')),
        field_filter(*('sport', 'volleyball')),
        field_filter('gender', 'male')
    )
    assert [] == value    


if __name__ == "__main__":
    test_query()

