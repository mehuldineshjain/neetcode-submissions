class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        the_hash = {}
        answer = []
        for i in range(0, len(nums)):
            required_number = target - nums[i]
            if required_number in the_hash:
                j = the_hash[required_number]
                return [min(i,j), max(i,j)]
            else:
                the_hash[nums[i]] = i

        