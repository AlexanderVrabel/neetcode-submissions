class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subtractions = {}
        for i, num in enumerate(nums):
            subtractions[num] = i

        for i in range(len(nums)):
            lookingfor = target-nums[i]
            if lookingfor in subtractions:
                if i == subtractions[lookingfor]:
                    continue
                return [min(i, subtractions[lookingfor]),max(i, subtractions[lookingfor])]
        