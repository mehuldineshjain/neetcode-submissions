class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest, left, right = 0, 0, 0
        length = len(s)
        hashed = {}
        window_size = 1
        max_length = 0
        max_count = 0
        while(right < length):
            r = s[right]
            l = s[left]

            # print(f"left: {left}, right: {right} l:{l}, r:{r}")
            # print(f"hashed: {hashed}")
            # print(f"max_count: {max_count}, max_length: {max_length}, window_size: {window_size} \n")
            if(r in hashed):
                hashed[r] += 1
            else:
                hashed[r] = 1
            max_count = max(max_count,hashed[r])
            if window_size - max_count <= k:
                max_length = max(window_size, max_length)
            else:
                hashed[l] -= 1
                left += 1
            right += 1
            window_size = (right - left) + 1

        return max_length
            
            
            
            
            # i = 0
            # {x : 1}
            
        


        