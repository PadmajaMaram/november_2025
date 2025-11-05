class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        while i<len(nums):
            count=1
            while i+1<len(nums) and nums[i]==nums[i+1]:
                count+=1
                i=i+1
            if(count==1):
                return nums[i]
            i=i+1


    
                    
        