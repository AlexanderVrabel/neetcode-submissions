class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = []
        for i, n in enumerate(nums):
            numbers.append([n, i])
        numbers.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            if numbers[i][0] + numbers[j][0] == target:
                return [min(numbers[i][1], numbers[j][1]), max(numbers[i][1], numbers[j][1])]
            elif numbers[i][0] + numbers[j][0] > target:
                j -= 1
            else:
                i += 1
