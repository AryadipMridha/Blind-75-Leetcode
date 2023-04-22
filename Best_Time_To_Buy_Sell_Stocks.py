class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Using Sliding window
        maxProfit=0
        leftPane , rightPane=0,1

        #while the prices array exists for the right pane to move
        
        while rightPane < len(prices):

            #we will check whether right Pane value is greater the the left pane or not
            if prices[leftPane] <= prices[rightPane]:
                maxProfit = max(maxProfit ,  prices[rightPane]-prices[leftPane]) 

            #if the prices dont increases and decreses instead
            while prices[leftPane] > prices[rightPane]:
                leftPane+=1
            #Right Pane Keeps on going increses no matter what
            rightPane+=1

        return maxProfit
