public class Solution {
    public int RemoveDuplicates(int[] nums) {
        int i = 0;
        foreach (int num in nums){
            if(i == 0 || i == 1 || nums[i-2] != num){
                nums[i] = num;
                i++;
            }
        }
        return i;
    }
}
