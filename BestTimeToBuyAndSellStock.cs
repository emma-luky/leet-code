public class Solution {
    public int MaxProfit(int[] prices) {
        int min = prices[0];
        int index = 0;
        for (int i = 1; i < prices.Length - 1; i++) {     
            Console.WriteLine(i);   
            if(prices[i] < min){
                min = prices[i];
                index = i;
            }
        }

        int max = 0;
        for (int i = index + 1; i < prices.Length; i++){
            if (prices[i] > max){
                max = prices[i];
            }
        }
        if (max - min < 0){
            return 0;
        }
        return max - min;
    }
}
