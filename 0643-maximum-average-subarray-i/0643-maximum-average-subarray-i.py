class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum1=sum(nums[:k])
        max_sum=sum1
        for i in range(k,len(nums)):
            sum1=sum1-nums[i-k]+nums[i]
            max_sum=max(max_sum,sum1)
        return max_sum/float(k)
        