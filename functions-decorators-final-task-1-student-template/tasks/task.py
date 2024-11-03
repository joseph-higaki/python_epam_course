from typing import List

def split(data: str, sep=None, maxsplit=-1):
    """
    Add your code here or call it from here   
    """
    sep = ' ' if not sep else sep
    result = []
    result_txt = data.strip()
    index = 0 
    splits = 0
    while index != -1 and result_txt and (maxsplit == -1 or splits < maxsplit):
        index = result_txt.find(sep)
        if index > -1:
            splits += 1
            #found sep
            #add before sep
            result.append(result_txt[:index])
            #remove before sep section for next iteration
            result_txt = result_txt[index + len(sep): ].strip()

    if data:
        #if the input parameter was empty, the result should be an empty list, thus not adding text
        #if the result_txt is empty but data was provided, it is the last iteration, should be added as an empty string after sep should be in the list
        result.append(result_txt[:len(result_txt)])
#    result_txt = ""
    return result    

    #print(first_token)
    #print(next_token)

    
def tests():
    assert split('1,123,re', sep=',') == ['1','123','re']
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']

if __name__ == '__main__':
    #a = split('1,123,re', sep=',')
    #print(a)
    tests()

    #split(',123,', sep=',')
    #split('    set   3     4')    
    #split('    set   3     4', sep='o')