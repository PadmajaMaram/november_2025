class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix1=[0]*len(nums)
        prefix1[0]=nums[0]
        for i in range(1,len(nums)):
            prefix1[i]=prefix1[i-1]+nums[i]
        a=min(prefix1)
        if a<1:
            return 1-a
        else:
            return 1


        