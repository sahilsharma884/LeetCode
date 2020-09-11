class Solution {
public:
    int singleNumber(vector<int>& nums) {
        // Use XOR operation to all elements
        // same number appear as zero which eliminates that number
        int result = nums[0];
        for (int i=1; i<nums.size();i++) {
            result ^= nums[i];
        }
        
        return result;
    }
};
