# You shouldn't change  name of function or their arguments
# but you can change content of the initial functions.
from argparse import ArgumentParser
from typing import List, Optional, Sequence, Callable 
import requests
import xml.etree.ElementTree as ElementTree
import json

class UnhandledException(Exception):
    pass

def do_optional(item: str, func: Callable):
    if item:
        func(item)

def do_caption_optional(item: str, caption: str, func: Callable) -> None:
    if item:
        func(f'{caption}: {item}')

class FeedItem:
    def __init__(self, 
                 title: str, 
                 description: str, 
                 author: Optional[str] = None, 
                 pub_date: Optional[str] = None, 
                 link: Optional[str] = None, 
                 category: Optional[List[str]] = None) -> None:
        self.title = title
        self.description = description
        self.author = author
        self.pub_date = pub_date
        self.link = link
        self.category = category


    def asdict(self):
        result = {
            'title': self.title,
            'author': self.author,
            'pubDate': self.pub_date,
            'link': self.link,
            'category': str(self.category),
            'description': self.description,
        }
        return {k: v for k, v in result.items() if v}        

class Feed:
    def __init__(self, 
                 title: str, 
                 link: str, 
                 description: str, 
                 items: List[FeedItem], 
                 last_build_date: Optional[str] = None, 
                 pub_date: Optional[str] = None, 
                 language: Optional[str] = None, 
                 category: Optional[List[str]] = None, 
                 managing_editor: Optional[str] = None) -> None:
        self.title = title
        self.link = link
        self.description = description
        self.items = items
        self.last_build_date = last_build_date
        self.pub_date = pub_date
        self.language = language
        self.category = category
        self.managing_editor = managing_editor

    def as_list_str(self) -> List[str]:
        result = []    
        do_caption_optional(self.title, 'Feed', result.append)
        do_caption_optional(self.link, 'Link', result.append)
        do_caption_optional(self.last_build_date, 'Last Build Date', result.append)
        do_caption_optional(self.pub_date, 'Publish Date', result.append)
        do_caption_optional(self.language, 'Language', result.append)
        if self.category is not None and 0 < len(self.category):
            result.append(','.join(self.category))
        do_caption_optional(self.managing_editor, 'Editor', result.append)
        do_caption_optional(self.description, 'Description', result.append)

        for item in self.items:
            result.append('\n')
            do_caption_optional(item.title, 'Title', result.append)
            do_caption_optional(item.author, 'Author', result.append)
            do_caption_optional(item.pub_date, 'Published', result.append)
            do_caption_optional(item.link, 'Link', result.append)
            if item.category is not None and 0 < len(item.category):
                result.append(','.join(item.category))         
            if item.description:
                result.append('\n')
                result.append(item.description)
        return result

    def asdict(self):
        result = {
            'title': self.title,
            'link': self.link,
            'lastBuildDate': self.last_build_date,
            'pubDate': self.pub_date,
            'language': self.language,
            'category': str(self.category),
            'managingEditor': self.managing_editor,
            'description': self.description,
            'items': [item.asdict() for item in self.items]              
        }
        return {k: v for k, v in result.items() if v}

def get_optional_item_text(item: ElementTree.Element) -> str:
    result = ""
    if item is not None:
        result = item.text
    return result

def print_feed_plain(feed: Feed) -> List[str]:
    return feed.as_list_str()

def spaces(n: int):
    return ' ' * n

def print_feed_json(feed_dict: dict, indent_level: int) -> List[str]:
    result = []   
    for idx, k in enumerate(feed_dict):
        #Iterate key values from dictionary
        if len(result) == 0:
            result.append(f'{spaces(indent_level)}'+'{')  
        separator = '' if idx == len(feed_dict) - 1 else ','
        if k != "items":
            result.append(f'{spaces(indent_level + 1)}"{k}": "{feed_dict[k]}"{separator}') if feed_dict[k] else ... 
        else:
            # if found an items dictionary list
            result.append(f'{spaces(indent_level + 1)}"{k}": [')
            
            for idx_item, item in enumerate(feed_dict["items"]):
                # iterate through each item on the list of dicts
                result_items = print_feed_json(item, indent_level + 2)
                separator_dict = '' if idx_item == len(feed_dict["items"]) - 1 else ','
                result_items[len(result_items) - 1] = result_items[len(result_items) - 1] + separator_dict
                result.extend(result_items)

            result.append(f'{spaces(indent_level + 1)}]')
    if 0 < len(feed_dict):            
        result.append(f'{spaces(indent_level)}'+'}')
    return result

def parse_multiple_items(items: List[ElementTree.Element]) -> List[str]:
    result = []
    for item in items:
        text = get_optional_item_text(item)
        if text and text not in result:
            result.append(text)
    return result

def parse_feed(root: ElementTree.ElementTree, limit: int) -> FeedItem:
    for feed in root.findall('channel'):
        title = get_optional_item_text(feed.find('title'))
        link = get_optional_item_text(feed.find('link'))
        last_build_date = get_optional_item_text(feed.find('lastBuildDate'))
        pub_date = get_optional_item_text(feed.find('pubDate'))
        language = get_optional_item_text(feed.find('language'))
        category = parse_multiple_items(feed.findall('category'))
        managing_editor = get_optional_item_text(feed.find('managingEditor'))
        description = get_optional_item_text(feed.find('description'))
        feed_items = []
        processed_items = 0
        for feed_item in feed.findall('item'):
            if limit is None or processed_items <= limit:                    
                feed_item_title = get_optional_item_text(feed_item.find('title'))
                feed_item_author = get_optional_item_text(feed_item.find('author'))
                feed_item_pub_date = get_optional_item_text(feed_item.find('pubDate'))
                feed_item_link = get_optional_item_text(feed_item.find('link'))
                feed_item_category = parse_multiple_items(feed_item.findall('category'))
                feed_item_description = get_optional_item_text(feed_item.find('description'))
                processed_items += 1
                feed_items.append(FeedItem(feed_item_title,
                                            feed_item_description, 
                                            feed_item_author, 
                                            feed_item_pub_date, 
                                            feed_item_link, 
                                            feed_item_category))
        
    result = Feed(title,
                    link,
                    description,
                    feed_items,
                    last_build_date, 
                    pub_date, 
                    language,
                    category,
                    managing_editor)
    return result

def rss_parser(
    xml: str,
    limit: Optional[int] = None,
    json: bool = False,
) -> List[str]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        >>> xml = '<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>'
        >>> rss_parser(xml)
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        >>> print("\\n".join(rss_parser(xmls)))
        Feed: Some RSS Channel
        Link: https://some.rss.com
    """    
    root = ElementTree.fromstring(xml)    
    feed = parse_feed(root, limit)    
    return print_feed_json(feed.asdict(), 0) if json else print_feed_plain(feed)   

    # Your code goes here

def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(args.source).text
    try:
        the_list = rss_parser(xml, args.limit, args.json)
        print("\n".join(the_list))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
