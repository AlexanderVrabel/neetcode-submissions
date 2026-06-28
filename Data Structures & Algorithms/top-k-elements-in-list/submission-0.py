class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = {}
        for i in nums:
            if i in numsDict:
                numsDict[i] += 1
            else:
                numsDict[i] = 1
            
        return sorted(numsDict, key=numsDict.get, reverse=True)[:k]