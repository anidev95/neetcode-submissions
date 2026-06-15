class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 1
        startingIndex = 0;
        while i < len(nums):
            if(sum([nums[i], nums[startingIndex]]) == target):
                return [startingIndex, i]
            elif(i == len(nums) - 1):
                startingIndex += 1
                i = startingIndex + 1
                continue
            i += 1
        return []