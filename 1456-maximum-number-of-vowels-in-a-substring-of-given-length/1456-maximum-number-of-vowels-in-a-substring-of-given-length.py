class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count=0
        arr=s[:k]
        for ch in arr:
            if ch in "aeiou":
                count+=1
        max_length=count
        left=0
        right=k
        while right<len(s):
            if s[left] in "aeiou":
                count-=1
            if s[right] in "aeiou":
                count+=1
            max_length=max(max_length,count)
            left+=1
            right+=1
        return max_length
        