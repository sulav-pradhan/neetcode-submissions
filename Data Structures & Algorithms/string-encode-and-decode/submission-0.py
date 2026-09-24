class Solution:

    def encode(self, strs: List[str]) -> str:
        # len#someencoding
        encoded_string = ""
        for string in strs: 
            length = len(string)
            encoded_string += str(length) + "#" + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        # ouput will be something like 5#hello
        decoded_str, i = [] , 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded_str.append(s[j+1: j+1+length])
            i = j + 1 + length
        return decoded_str

            
