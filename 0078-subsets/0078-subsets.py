class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a=[[]]
        for num in nums:
            sub=[]
            for res in a:
                sub.append(res+[num])
            a.extend(sub)
        return a



