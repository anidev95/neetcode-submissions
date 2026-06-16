class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = 0
        products = []
        while x < len(nums):
            newLst = nums[0:x] + nums[x+1:]
            product = 1
            for i in newLst:
                product *= i
            products.append(product)
            x += 1
        return products
