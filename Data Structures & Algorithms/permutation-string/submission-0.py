class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        left, right = 0, len1 - 1
        s1_count = self.count_it(s1)
        # print(f"left: {left}, right: {right}")
        # print(f"s1_count: {s1_count}")
        while(right < len(s2)):
            if(s2[left] not in s1_count):
                left += 1
                right += 1
                # print(f"increased left: {left}, right: {right}")
                continue
            else:
                dict_of_sub = self.count_it(s2[left:right + 1])
                # print(f"dict_of_sub: {dict_of_sub}")
                if dict_of_sub == s1_count:
                    return True
            left += 1
            right += 1
            # print(f"left: {left}, right: {right}")
        return False

    def count_it(self, s: str) -> dict:
        count = {}
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        return count