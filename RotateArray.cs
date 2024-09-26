public class Solution {
    public void Rotate(int[] nums, int k) {
        while (k > nums.Length){
            k = k - nums.Length;
        }
        int[] rotatedArray = new int[nums.Length];
        for (int i = 0; i < nums.Length; i++){
            if(i < nums.Length - k){
                rotatedArray[i + k] = nums[i];
            }
            else{
                int index = i + k - nums.Length;
                while (index > nums.Length){

                }
                rotatedArray[i + k - nums.Length] = nums[i];
            }
        }
        for (int i = 0; i < nums.Length; i ++) {
            nums[i] = rotatedArray[i];
        }
    }
}
