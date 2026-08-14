class Solution:
    # def trap(self, height: List[int]) -> int:
    #     # [0,2,0,3,1,0,1,3,2,1]
    #     # left_max = [0, 0, 2, 2, 3, 3, 3, 3, 3, 3]
    #     # right_max = [3, 3, 3, 3, 3, 3, 3, 2, 1, 0]

    #     # left_max = 3, right_max = 3, min = 3, height[4] = 1
    #     # min(max_left,max_right) - height = 2

    #     length = len(height)
    #     maximum = 0
    #     max_left = [0] * length
    #     max_right = [0] * length
    #     i = 1
    #     result = 0
    #     while(i < length):
    #         max_left[i] = max(maximum, height[i-1])
    #         maximum = max_left[i]
    #         i += 1
        
    #     i = length - 2
    #     maximum = 0
        
    #     while(i >= 0):
    #         max_right[i] = max(maximum, height[i + 1])
    #         maximum = max_right[i]
    #         i -= 1
        
    #     for i in range(1, length - 1):
    #         result += max(0, (min(max_left[i],max_right[i]) - height[i]))
    #     print(max_left)
    #     print(max_right)
    #     return result




















    def trap(self, height: List[int]) -> int:
        # heights =   [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
        # left_max =  [0, 0, 2, 2, 3, 3, 3, 3, 3, 3] = 22 
        # right_max = [3, 3, 3, 3, 3, 3, 3, 2, 1, 0]

        # left_max = 3, right_max = 3, min = 3, height[4] = 1
        # min(max_left,max_right) - height = 2
        # find the minimum of the leftmax and rightmax and subtract the height from it
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = 0
        for i in range(1,n):
            left_max[i] = max(left_max[i-1], height[i-1])
        right_max[-1] = 0
        total = 0
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i+1])
        
            total += max(0, (min(left_max[i],right_max[i]) - height[i]))
        return total

























