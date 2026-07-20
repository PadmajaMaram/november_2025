class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res=[0]*len(code)
        arr=code*2
        list1=[]
        if k==0:
            return res
        elif k>0:
            sum1=sum(arr[1:k+1])
            for i in range(len(code)):
                list1.append(sum1)
                sum1 += arr[i+k+1]-arr[i+1]
        else:
            sum2=sum(arr[len(code)+k:len(code)])
            for i in range(len(code)):
                list1.append(sum2)
                sum2+=arr[len(code)+i]-arr[len(code)+k+i]
        return list1