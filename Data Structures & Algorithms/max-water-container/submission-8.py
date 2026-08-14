class Solution:
    # def maxArea(self, heights: List[int]) -> int:
    #     p1 = 0
    #     p2 = length - 1
    #     # mid used only as reference point
    #     max_area = 0
    #     while(p1 < p2):
    #         area = min(heights[p1], heights[p2]) * (p2 - p1)
    #         max_area = max(max_area, area)
    #         if(heights[p1] < heights[p2]):
    #             p1 += 1
    #         # elif (heights[p2] < heights[p1]):
    #         #     p2 -= 1
    #         # elif(heights[p1 + 1] > heights[p2 - 1]):
    #         #     p2 -= 1
    #         # else:
    #         #     p1 += 1
    #         else: 
    #             p2 -= 1
    #     return max_area

            

    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(heights) - 1
        while(l<r):
            area = (r - l) * min(heights[l], heights[r])
            max_area = max(area, max_area)
            if(heights[l] > heights[r]):
                r -= 1
            elif(heights[l] < heights[r]):
                l += 1
            else:
                l += 1
        return max_area






















