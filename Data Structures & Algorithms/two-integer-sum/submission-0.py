class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}
        for i, num in enumerate(nums):
            j = target - num
            if j in num_set:
                return [num_set[j], i]
            num_set[num] = i
