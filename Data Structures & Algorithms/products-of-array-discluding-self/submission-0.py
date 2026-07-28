class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output_array = [1] * length
        prefix = 1
        postfix = 1
        for i in range(0,length): 
            output_array[i] = prefix
            prefix *= nums[i]
        for i in range(length - 1, -1, -1):
            output_array[i] *= postfix 
            postfix *= nums[i]
        return output_array




