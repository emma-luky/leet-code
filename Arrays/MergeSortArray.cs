public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        int i1 = m - 1;  // Last element in nums1 that is part of the sorted section
        int i2 = n - 1;  // Last element in nums2
        int index = m + n - 1;  // Last position of nums1
        
        while (i1 >= 0 && i2 >= 0) {
            if (nums1[i1] > nums2[i2]) {
                nums1[index] = nums1[i1];
                i1--;
            } else {
                nums1[index] = nums2[i2];
                i2--;
            }
            index--;
        }
        
        while (i2 >= 0) {
            nums1[index] = nums2[i2];
            i2--;
            index--;
        }
    }
}
