#from dict_based_pagination import DictPagination
from math import ceil 

class Pagination:    
    def __init__(self, data: str, items_on_page: int):
        self.data = data
        self.items_on_page = items_on_page
        #self.pages = {page: data[start_index:start_index + self.items_on_page] for page, start_index in enumerate(range(0, len(self.data), self.items_on_page))}

    @property
    def item_count(self):
        return len(self.data)
    
    @property
    def page_count(self):
        return int(ceil(len(self.data) / self.items_on_page))
    
    def display_page(self, page_number): 
        if self.page_count <= page_number:
            raise Exception("Invalid index. Page is missing.")
        from_index = page_number * self.items_on_page
        to_index = min(from_index + self.items_on_page, len(self.data))
        return self.data[from_index:to_index]

    def count_items_on_page(self, page_number):        
        return len(self.display_page(page_number))

    def find_page(self, word):
        if not word in self.data:
            raise Exception(f"'{word}' is missing on the pages")
        result = []
        start_index = 0
        while 0 <= start_index and start_index < len(self.data):            
            start_index = self.data.find(word, start_index)
            if 0 <= start_index:
                to_index = start_index + len(word)
                for index in range(start_index, to_index, self.items_on_page):
                    result.append(index // self.items_on_page)                                   
                start_index = to_index            
        return result  

def tests():
    pages = Pagination('Your beautiful text', 5)
    assert pages.page_count == 4
    assert pages.item_count == 19
    assert pages.count_items_on_page(0) == 5
    assert pages.count_items_on_page(3) == 4
    try:
        print(pages.count_items_on_page(4))
    except Exception as e: 
        assert str(e) == "Invalid index. Page is missing." 

    assert pages.find_page('Your') == [0]
    assert pages.find_page('e') == [1, 3]
    assert pages.find_page('beautiful') == [1, 2]
    try:
        print(pages.find_page('great'))
    except Exception as e: 
        assert str(e) == "'great' is missing on the pages" 
    
    assert pages.display_page(0) == 'Your '

    pages = Pagination('Y', 5)
    assert pages.page_count == 1 


if __name__ == "__main__":
    tests()
    