class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            max1=max(nums[:i+1])
            min1=min(nums[i:])
            if (max1-min1)<=k:
                return i
        return -1
        