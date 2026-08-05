class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        length = len(heights)
        p2 = length - 1
        # mid used only as reference point
        max_area = 0
        while(p1 < p2):
            area = min(heights[p1], heights[p2]) * (p2 - p1)
            max_area = max(max_area, area)
            if(heights[p1] < heights[p2]):
                p1 += 1
            # elif (heights[p2] < heights[p1]):
            #     p2 -= 1
            # elif(heights[p1 + 1] > heights[p2 - 1]):
            #     p2 -= 1
            # else:
            #     p1 += 1
            else: 
                p2 -= 1
        return max_area

            
