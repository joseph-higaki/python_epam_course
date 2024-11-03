class DictPagination:    
    def __init__(self, data: str, items_on_page: int):
        self.data = data
        self.items_on_page = items_on_page
        self.pages = {page: data[start_index:start_index + self.items_on_page] for page, start_index in enumerate(range(0, len(self.data), self.items_on_page))}

    @property
    def item_count(self):
        return len(self.data)
    
    @property
    def page_count(self):
        return len(self.pages)

    def count_items_on_page(self, page_number):
        return len(self.display_page(page_number))

    def find_page(self, data):
        result = [k for k, v in self.pages.items() if v.find(data) >= 0]
        if not result:
            raise Exception(f"'{data}' is missing on the pages")
        return result
    
    def display_page(self, page_number):
        try:
            result = self.pages[page_number]
        except KeyError:
            raise Exception("Invalid index. Page is missing.")
        return result