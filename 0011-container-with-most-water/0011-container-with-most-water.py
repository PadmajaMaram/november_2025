class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        right=len(height)-1
        left=0
        max_val=0
        while left<right:
            width=right-left
            h=min(height[left],height[right])
            ans=width*h
            max_val=max(max_val,ans)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1 
        return max_val   