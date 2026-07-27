class Solution:
    def countBits(self, n: int) -> List[int]:
        list1=[]
        for i in range(n+1):
            count=0
            while i!=0:
                if i&1:
                    count+=1
                i=i>>1
            list1.append(count)
        return list1