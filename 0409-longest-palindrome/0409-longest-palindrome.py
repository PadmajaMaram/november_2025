class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap1={}
        if len(s)==1:
            return 1
        for ch in s:
            if ch in hashmap1:
                hashmap1[ch]+=1
            else:
                hashmap1[ch]=1
        count=0
        if len(hashmap1)==1:
            return len(s)
        hasodd=False
        for value in hashmap1.values():
            if value%2==0:
                count+=value
            else:
                count+=value-1
                hasodd=True
        if hasodd:
            count+=1
        return (count)


        
        