class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict1={}
        dict2={}
        for ch in magazine:
            if ch in dict1:
                dict1[ch]+=1
            else:
                dict1[ch]=1
        for ch in ransomNote:
            if ch in dict2:
                dict2[ch]+=1
            else:
                dict2[ch]=1
        for ch in dict2:
            if ch not in dict1 or dict2[ch]>dict1[ch]:
                return False
        return True
                

        