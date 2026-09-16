UPPER_LIMIT = 1000

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        return [x[0] for x in cnt.most_common(k)]





        # freq = {}
        # for num in nums:
        #     if num in freq:
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1   

        # freq_sort = [None] * (len(nums) + 1)
        
        # for key, val in freq.items():
        #     if freq_sort[val]:
        #         freq_sort[val].append(key)
        #     else:
        #         freq_sort[val] = [key]

        
        # i = len(nums)
        # topk_freq = []
        # while k>0 and i >=0:
        #     if freq_sort[i]:
        #         for val in freq_sort[i]:
        #             topk_freq.append(val)
        #             k -= 1
        #     i -= 1
        # return topk_freq


