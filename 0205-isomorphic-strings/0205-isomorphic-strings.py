class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap1={}
        for i in range(len(s)):
            if s[i] in hashmap1:
                if hashmap1[s[i]]!=t[i]:
                        return False
            else:
                if t[i] in hashmap1.values():
                    return False
                hashmap1[s[i]]=t[i]
        return True
        