class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        valid_parenthesis={"}":"{",")":"(","]":"["}
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack or stack.pop()!=valid_parenthesis[ch]:
                    return False
        return not stack