class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,2,0,3,1,0,1,3,2,1]
        # left_max = [0, 0, 2, 2, 3, 3, 3, 3, 3, 3]
        # right_max = [3, 3, 3, 3, 3, 3, 3, 2, 1, 0]

        # left_max = 3, right_max = 3, min = 3, height[4] = 1
        # min(max_left,max_right) - height = 2

        length = len(height)
        maximum = 0
        max_left = [0] * length
        max_right = [0] * length
        i = 1
        result = 0
        while(i < length):
            max_left[i] = max(maximum, height[i-1])
            maximum = max_left[i]
            i += 1
        
        i = length - 2
        maximum = 0
        
        while(i >= 0):
            max_right[i] = max(maximum, height[i + 1])
            maximum = max_right[i]
            i -= 1
        
        for i in range(1, length - 1):
            result += max(0, (min(max_left[i],max_right[i]) - height[i]))
        print(max_left)
        print(max_right)
        return result