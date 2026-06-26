class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort(reverse=True)
        money1=money
        count=0
        for i in range(len(prices)-1,-1,-1):
            if money>=prices[i]:
                money=money-prices[i]
                count+=1
                if count==2:
                    return money
        if count<2:
            return money1
    
