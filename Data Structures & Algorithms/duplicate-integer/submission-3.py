class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        x = 1
        dup = 0
        while(x < len(nums)):
            if(nums[x] == nums[x-1]):
                return True
            x += 1
        return False