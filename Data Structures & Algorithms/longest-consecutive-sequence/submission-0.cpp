#include <vector>
#include <algorithm>
#include <iostream>



class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        if(nums.empty())return 0;

        sort(nums.begin(),nums.end());

        int maxSequenceLen = 1;
    int currentSequenceLen = 1; // Tracks current connected chain

    // 2. Loop safely from index 1 (comparing i with i - 1)
    for (int i = 1; i < nums.size(); ++i) {
        
        // Handle Trap #4: Skip duplicates
        if (nums[i] == nums[i - 1]) {
            continue;
        }

        // Handle Trap #3: Match found! Add to CURRENT chain length
        if (nums[i] - nums[i - 1] == 1) {
            currentSequenceLen++;
        } 
        // Handle Trap #2: Gap found! Save best length and RESET counter
        else {
            maxSequenceLen = max(maxSequenceLen, currentSequenceLen);
            currentSequenceLen = 1; 
        }
    }

    return max(maxSequenceLen, currentSequenceLen);
}



        
};

