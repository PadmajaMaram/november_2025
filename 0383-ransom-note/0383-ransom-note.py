class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap={}
        for ch in magazine:
            if ch not in hashmap:
                hashmap[ch]=1
            else:
                hashmap[ch]+=1
        for ch in ransomNote:
            if ch in hashmap:
                hashmap[ch]-=1
                if hashmap[ch]<0:
                    return False
            else:
                return False
        return True


        