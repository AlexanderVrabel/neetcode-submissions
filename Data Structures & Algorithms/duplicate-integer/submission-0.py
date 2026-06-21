class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Map = {}
        for num in nums:
            if num not in Map:
                Map[num]=1
            else:
                return True
        return False