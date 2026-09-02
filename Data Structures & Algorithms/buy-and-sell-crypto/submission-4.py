class Solution: #using two pointers as continuous range not required here unlike heading pattern recognition is imp rather than following a specific heading
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        profit = 0
        while right <= len(prices)-1:
            if prices[right] - prices[left] > profit:   
                profit = prices[right]- prices[left]

            if prices[right] < prices[left]:
                left = right
            right += 1
        return profit

# or use below code- same logic with else 

class Solution: #refer notes
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left + 1
        profit = 0
        while right <= len(prices) - 1:
            if prices[right] < prices[left]:
                left = right
            else:
                profit = max(profit,prices[right] - prices[left] )
            right += 1
        return profit