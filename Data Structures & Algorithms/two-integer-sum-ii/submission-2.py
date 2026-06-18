class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        print(numbers)
        for i in range(len(numbers)):
            for x in range(i+1, len(numbers)):
                if(numbers[i] + numbers[x] == target):
                    return [i+1, x+1]
        return []