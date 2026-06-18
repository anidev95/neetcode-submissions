class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        print(numbers)
        i = 0
        s = 1
        while(i < len(numbers)):
            print('i: ' + str(i) + ' numbers[i]: ' + str(numbers[i]) + "\ns: " + str(s) + ' numbers[s]: ' + str(numbers[s]))
            print(numbers[i] + numbers[s] == target)
            if(s != i and (numbers[i] + numbers[s] == target)):
                return [i+1, s+1]
            elif(s == len(numbers) - 1):
                i += 1
                s = i - 1
            else:
                s += 1
        return []