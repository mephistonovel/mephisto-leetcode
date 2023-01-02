class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // int index1;
        // int index2;
        vector<int> answer(2);
        
        int num1;
        int num2;
        bool check=0;
        for (int i=0;i<nums.size();i++){
            num1 = nums[i];
            num2 = target - num1;
            for (int j=0;j<nums.size();j++){
                if ((num2==nums[j]) && (i!=j)){
                    answer[0] = i;
                    answer[1] = j;
                    check=1;
                    break;
                }
            }
            if (check){
                break;
            }
        }
        
        return answer;
    }
};