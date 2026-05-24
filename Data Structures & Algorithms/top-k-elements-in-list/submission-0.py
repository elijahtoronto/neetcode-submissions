from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = Counter(nums)
        top_num = groups.most_common(k)
        return [pair[0] for pair in top_num]