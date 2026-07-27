class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        array_1 = [0] * 26
        array_2 = [0] * 26
        for i in s:
            array_1[(ord(i) - 97)] += 1
        for j in t:
            array_2[(ord(j) - 97)] += 1
        
        # print(array_1)
        # print(array_2)
        return array_1 == array_2