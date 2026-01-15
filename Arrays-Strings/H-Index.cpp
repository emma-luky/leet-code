class Solution {
public:
    int hIndex(vector<int>& citations) {
        int maximum = citations.size();
        int hIndex = 0;
        sort(citations.begin(), citations.end());
         for (int i = 0; i < citations.size(); i++){
            if (citations[i] >= maximum - i){
                hIndex = max(hIndex, maximum - i);
            }
         } return hIndex;
    }
};
