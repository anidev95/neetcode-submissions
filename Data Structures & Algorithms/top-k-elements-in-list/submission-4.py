from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        lst = []
        for num in nums:
            if(num in freq):
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1
        i = 0
        sorted_dict = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        for key, value in sorted_dict.items():
            if(i < k):
                lst.append(key)
            else:
                break
            i += 1
        return lst