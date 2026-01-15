public class Solution {
    public int MajorityElement(int[] nums) {
        Dictionary<int,int> map = new Dictionary<int, int>();
        foreach(int num in nums){
            if(map.ContainsKey(num)){
                map[num]++;
            }
            else{
                map.Add(num, 1);
            }
        }
        int max = 0;
        int key = 0;
        foreach(var item in map){
            if(item.Value > nums.Length / 2 && item.Value > 0){
                key = item.Key;
            }
        }
        return key;
    }
}
