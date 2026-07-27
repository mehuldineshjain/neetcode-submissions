class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        sort_hash = {}
        for string in strs:
            if string == "":
                the_key = "."
            else:
                the_key = self.key_maker(string)
            if the_key in sort_hash:
                sort_hash[the_key].append(string)
            else:
                sort_hash[the_key] = [string]
        return list(sort_hash.values())


    def key_maker(self, string: str) -> str:
        print(string)
        key = ""
        order_array = [0]*26
        for s in string:
            order_array[ord(s) - 97] += 1
        key = ",".join(str(a) for a in order_array)
        return key
    
    