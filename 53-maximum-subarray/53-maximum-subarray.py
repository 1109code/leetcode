class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i-1] if nums[i-1] > 0 else 0
        return max(nums)