class Solution:
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     len1, len2 = len(s1), len(s2)
    #     left, right = 0, len1 - 1
    #     s1_count = self.count_it(s1)
    #     while(right < len(s2)):
    #         if(s2[left] not in s1_count):
    #             left += 1
    #             right += 1
    #             continue
    #         else:
    #             dict_of_sub = self.count_it(s2[left:right + 1])
    #             if dict_of_sub == s1_count:
    #                 return True
    #         left += 1
    #         right += 1
    #     return False

    # def count_it(self, s: str) -> dict:
    #     count = {}
    #     for i in s:
    #         if i in count:
    #             count[i] += 1
    #         else:
    #             count[i] = 1
    #     return count


    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        left, right = 0, len1 - 1
        
        key = self.convert_it(s1)

        while(right < len2):
            new_key = self.convert_it(s2[left:right + 1])
            if new_key == key:
                return True
            left += 1
            right += 1
        return False

    def convert_it(self, s1):
        alpha = [0] * 26
        for i in s1:
            alpha[ord(i) - 97] += 1
        return alpha

