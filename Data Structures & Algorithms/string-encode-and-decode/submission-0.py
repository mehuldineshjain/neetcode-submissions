class Solution:

    def encode(self, strs: List[str]) -> str:
        # I can start with the first digits before a delimiter being number of strings
        # the following sets will mark every string beginning with the length of string
        final_string = ""
        delimiter = '.'
        for string in strs:
            length = len(string)
            new_string = f"{length}#"
            for s in string:
                new_string += str(ord(s) + length) + delimiter
            final_string += new_string
        print(final_string)
        return final_string

    def decode(self, s: str) -> List[str]:
        length = len(s)
        string_array = []
        x = 0
        for i in range(0, length):
            if s[i] == '#':
                len_of_string = int(s[x:i])
                i += 1
                string = ""
                temp = len_of_string
                while(temp):
                    temp -= 1
                    j = i
                    while(s[j] != '.'):
                        j += 1
                    string += chr(int(s[i:j]) - len_of_string)
                    i = j+1
                string_array.append(string)
                x = i
        return string_array