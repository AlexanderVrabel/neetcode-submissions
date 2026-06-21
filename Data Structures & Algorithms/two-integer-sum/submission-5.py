class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i,n in enumerate(nums):
            x = target - n
            if x in numsDict:
                return([min(numsDict[x],i), max(numsDict[x],i)])
            else:
                numsDict[n] = i