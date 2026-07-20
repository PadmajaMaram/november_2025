class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l=0
        count=0
        prod=1
        for i in range(len(nums)):
            prod*=nums[i]
            while prod>=k and l<=i:
                prod//=nums[l]
                l+=1
            count+=(i-l+1)
        return count


        