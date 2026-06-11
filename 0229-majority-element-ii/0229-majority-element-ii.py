class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        dict1={}
        for ch in nums:
            if ch in dict1:
                dict1[ch]+=1
            else:
                dict1[ch]=1
        a=[]
        for cha in dict1:
            if dict1[cha]>n/3:
                a.append(cha)
        return a 


        