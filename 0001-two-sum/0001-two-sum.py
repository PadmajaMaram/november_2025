class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for index,value in enumerate(nums):
            a=target-value
            if a in seen:
                return (seen[a],index)
            seen[value]=index
        return []
        