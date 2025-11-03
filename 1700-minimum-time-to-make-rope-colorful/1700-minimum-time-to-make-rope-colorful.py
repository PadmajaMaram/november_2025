class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        a=0
        for i in range(len(colors)-1):
            if colors[i]==colors[i+1]:
                a+=min(neededTime[i], neededTime[i+1])
                neededTime[i+1]=max(neededTime[i], neededTime[i+1])
        return(a)
        