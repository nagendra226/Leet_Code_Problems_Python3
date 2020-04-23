class Solution:
    def searchInsert(self, nums, target: int) -> int:
        count = 0
        if (target in nums):
            return nums.index(target)
        else:
            new_li = nums[:]
            new_li.append(target)
            new_li.sort()
            return new_li.index(target)
