class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0 
        for i in range(len(accounts)):
            sumCustomer = 0
            for j in range(len(accounts[i])):
                sumCustomer += accounts[i][j]
                maxWealth = max(maxWealth, sumCustomer)
        return maxWealth

        