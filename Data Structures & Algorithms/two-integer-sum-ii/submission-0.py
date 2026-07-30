class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # # Binary Search Solution 
        # left = 0
        # length = len(numbers)
        # right = length - 1
        # while(left < right):
        #     mid = int((left + right) / 2)
        #     new_sum = numbers[left] + numbers[right]
        #     if(new_sum == target):
        #         return [left + 1,right + 1]
        #     elif(new_sum < target):
        #         left = mid
        #     else:
        #         right = mid
        # return []
        
        
        # Hash map solution
        hash_sum = {}
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if tmp in hash_sum:
                return [hash_sum[tmp], i + 1]
            hash_sum[numbers[i]] = i + 1
        print(hash_sum)
        return []


        # # Two pointer solution

        