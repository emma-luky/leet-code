class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        for (int i = 1; i < prices.size(); i++) {
            int buy = prices[i-1];
            if (prices[i] > buy) {
                maxProfit += prices[i] - buy;
            }
        }
        return maxProfit;
    }
};
