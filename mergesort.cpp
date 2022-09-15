/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <vector>

using namespace std;
vector<int> sortArray(vector<int>& nums) {
        int len = nums.size();
        if (len<2){
            return nums;
        }
        
        int mid = (len-1)/2 ; // 
        vector<int> nums1(mid+1); //절반1
        vector<int> nums11(mid+1);
        
        vector<int> nums2(len-mid-1); // 절반2
        vector<int> nums22(len-mid-1);
        
        vector<int> nums33(len);
        
        for (int i=0;i<(mid+1);i++){
            nums1[i] = nums[i];
        }
        
        for (int j=0;j<(len-mid-1);j++){
            nums2[j]=nums[j+mid+1];
        }
        
        nums11 = sortArray(nums1);
        nums22 = sortArray(nums2);
        
        int i1 = 0;
        int i2= 0;
        int t=0;
        
        while ((i1<(mid+1)) && (i2<(len-mid-1))){
            if (nums11[i1]<nums22[i2]){
                nums33[t] = nums11[i1];
                t++;i1++;
            }
            else{
                nums33[t] = nums22[i2];
                t++;i2++;
            }
        }
        
        if (i1<(mid+1)){
            for (int r=t;r<len;r++){
                nums33[r] = nums11[i1];
                i1++;
            }
        }
        
        if (i2<(len-mid-1)){
            for (int r=t;r<len;r++){
                nums33[r] = nums22[i2];
                i2++;
            }
        }
        
        
        return nums33;
 }

int main()
{   vector<int> A = {4,2,3,1};
    vector<int> B(4);
    int n = A.size();
    cout<<n<<endl;
    B=sortArray(A);
    for (int i=0;i<4;i++){
        cout<<B[i]<<endl;
    }

    return 0;
}
