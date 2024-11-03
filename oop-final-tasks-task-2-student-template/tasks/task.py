class Cipher:    

    _STANDARD_ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    @staticmethod
    def __generate_cypher_alphabet(cipher_keyword: str) -> str:        
        result = Cipher._STANDARD_ALPHABET.copy()
        cipher_keyword_list = []
        for c in cipher_keyword:
            if c in result: 
                #Thus ignoring duplicates, whitespaces and non alphabet chars
                result.remove(c)        
                cipher_keyword_list.append(c)
        return cipher_keyword_list + result 
    
    def __init__(self, cypher_keyword: str) -> None:
        self.cipher_keyword = cypher_keyword.upper()
        self.cipher_alphabet = Cipher.__generate_cypher_alphabet(self.cipher_keyword)

    @staticmethod
    def __get_character(char: str, source_alphabet: list[str], destination_alphabet: list[str]):
        index = -1
        result = char
        if char.upper() in source_alphabet:
            index = source_alphabet.index(char.upper())        
        if -1 < index:
            result = destination_alphabet[index]
            result = result.upper() if char.isupper() else result.lower()
        return result

    @staticmethod  
    def __transcode(phrase: str, source_alphabet: list[str], destination_alphabet: list[str]):
        return ''.join([ Cipher.__get_character(char, source_alphabet, destination_alphabet) for char in phrase ])

    def encode(self, data):
        return Cipher.__transcode(data, Cipher._STANDARD_ALPHABET, self.cipher_alphabet)
    
    def decode(self, data):
        return Cipher.__transcode(data, self.cipher_alphabet, Cipher._STANDARD_ALPHABET)


def tests():
    cipher = Cipher("crypto")
    a=  cipher.encode("Hello world")
    print(a)
    assert cipher.encode("Hello world") == "Btggj vjmgp"
    assert cipher.decode("Fjedhc dn atidsn") == "Kojima is genius"

    

if __name__ == "__main__":
    tests()