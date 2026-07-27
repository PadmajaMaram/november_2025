class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack=[]
        for ch in asteroids:
            while stack and stack[-1]>0 and ch<0:
                if stack[-1]<-ch:
                    stack.pop()
                    continue
                elif stack[-1]==-ch:
                    stack.pop()
                break
            else:
                stack.append(ch)
        return stack
                    
        