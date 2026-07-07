class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        n=len(candyType)
        a=n//2
        hashmap={}
        for ch in candyType:
            if ch not in hashmap:
                hashmap[ch]=1
        if len(hashmap)>=a:
            return a
        else:
            return len(hashmap)

        