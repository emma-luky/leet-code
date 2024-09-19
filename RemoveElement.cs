public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int beginning = 0;
        if (Array.IndexOf(nums, val) < 0 && nums.Length == 0){
            return 0;
        }
        for (int i = 0; i < nums.Length; i++){
            if(nums[i] != val){
                int temp = nums[beginning];
                nums[beginning] = nums[i];
                nums[i] = temp;
                beginning++;
            }
        }
        return beginning;
    }
}
