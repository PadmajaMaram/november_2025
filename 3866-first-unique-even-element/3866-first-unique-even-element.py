class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap1={}
        for num in nums:
            if num in hashmap1:
                hashmap1[num]+=1
            else:
                hashmap1[num]=1
        for num in nums:
            if num%2==0 and hashmap1[num]==1:
                return num
        return -1

        