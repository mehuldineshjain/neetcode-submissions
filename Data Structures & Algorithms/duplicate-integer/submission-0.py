class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        the_hash = {}
        for i in nums:
            if i in the_hash:
                return True
            else:
                the_hash[i] = 1
        return False
        