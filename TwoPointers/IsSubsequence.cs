public class Solution {
    public bool IsSubsequence(string s, string t) {
        int beginning = 0;
        if(String.IsNullOrEmpty(s)){
            return true;
        }
        for (int j = 0; j < s.Length; j++){
            for (int i = beginning; i < t.Length; i++){
                if (j == s.Length - 1 && s[j] == t[i]){
                    return true;
                }
                else if (s[j] == t[i]){
                    beginning = i + 1;
                    break;
                }
                else if (i == t.Length - 1) {
                    return false;
                }
            }
        }
        return false;
    }
}
