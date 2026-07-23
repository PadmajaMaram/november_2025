class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        '''d={}
        stack=[]
        for ch in s:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
            stack.append(ch)
            if d[ch]>=k:
                del stack[-k:]
                del d[ch]
        return stack'''
        stack=[]
        for ch in s:
            if stack and stack[-1][0]==ch:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([ch,1])
        ans=""
        for ch,count in stack:
            ans+=ch*count
        return ans
            


        