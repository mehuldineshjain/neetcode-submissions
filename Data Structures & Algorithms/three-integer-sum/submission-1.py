class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums) -1
        answer_array = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            left, right = i + 1, length
            while(left < right):
                new_sum = a + nums[left] + nums[right]
                if new_sum < 0:
                    left += 1
                elif new_sum > 0:
                    right -= 1
                else:
                    answer_array.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while(nums[left] == nums[left - 1] and left < right):
                        left += 1
        return answer_array
