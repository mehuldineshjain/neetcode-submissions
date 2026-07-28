class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hash = {}
        count_array = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            if n in count_hash:
                count_hash[n] += 1
            else:
                count_hash[n] = 1
        for num,frequency in count_hash.items():
            count_array[frequency].append(num)
        res = []
        for freq in range(len(count_array) - 1, 0, -1):
            for num in count_array[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        