
#include <iostream>
#include <vector>

using namespace std;


void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    int i1 = 0;
    int i2 = 0;
    int i3=0;
    vector<int> res(m+n);

    while (i1<m && i2 <n){
        if (nums1[i1]<nums2[i2]){
            res[i3]=nums1[i1];
            i1++; i3++;
        }
        else if (nums1[i1] == nums2[i2]){
            res[i3]=nums1[i1];
            i3++;

            res[i3]=nums2[i2];

            i1++; i2++; i3++;
        }
        else{
            res[i3]=(nums2[i2]);
            i2++; i3++;
        }
    }

    
    if (i1>= m) {
        for (int i = i3;i<(m+n);i++){
            res[i]=nums2[i2];
            i2++;
        }
    }
    else {
        for (int i = i3;i<(m+n);i++){
            res[i]=nums1[i1];
            i1++;
        }
    }

    for (int r=0; r<(m+n); r++){
        nums1[r]=res[r];
    }
}

int main(){
    vector<int> m1={1,4,6,8,0,0,0};
    vector<int> m2={1,2,3};
    merge(m1,4,m2,3);
    for(int i=0; i<7; i++){
        cout<<m1[i]<<' ';
    }
    // output: 1123468
    cout<<endl;
}