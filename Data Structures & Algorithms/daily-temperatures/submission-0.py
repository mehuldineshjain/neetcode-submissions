class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoStack = []
        length = len(temperatures)
        resultStack = [0] * length
        for i in range(length):
            days = 0
            while(monoStack and temperatures[monoStack[-1]] < temperatures[i]):
                resultStack[monoStack[-1]] = (i - monoStack[-1])
                monoStack.pop()
            monoStack.append(i)
        return resultStack
        