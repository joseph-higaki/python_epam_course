from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    """
    Add your code here or call it from here   
    """
    indexes.sort()
    result = []
    text = s
    trimmed_text = 0
    for index in indexes:
        if 0 <= index and index <= len(s):
            token = text[:index - trimmed_text]
            trimmed_text += len(token)
            result.append(token)
            text = text[len(token):]
    result.append(text)
    return result

def tests():
    assert split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]) == ["python", "is", "cool", ",", "isn't", "it?"]
    assert split_by_index("no luck", [42]) == ["no luck"]

if __name__ == '__main__':    
    tests()