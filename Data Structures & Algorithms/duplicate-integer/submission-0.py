class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        clean_box = set(nums)
        return len(nums) != len(clean_box)