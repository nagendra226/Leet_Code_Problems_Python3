class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a, i in enumerate(nums):
            for b, j in enumerate(nums):
                if (i + j == target and a != b):
                    return (a, b)
