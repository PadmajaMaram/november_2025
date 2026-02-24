class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x)
        rev=int(str(x)[::-1])
        if rev<-2**31 or rev >2**31 -1 :
            return 0
        return sign*rev
