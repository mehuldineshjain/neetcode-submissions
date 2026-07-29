import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        p1 = 0
        p2 = length - 1
        while(p1 < p2):
            if not(re.search("[0-9a-zA-Z]", s[p1])):
                p1 += 1
                continue
            if not(re.search("[0-9a-zA-Z]", s[p2])):
                p2 -= 1
                continue
            if(s[p1].lower() != s[p2].lower()):
                return False
            p1 += 1
            p2 -= 1
        return True