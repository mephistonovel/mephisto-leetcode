// https://github.com/keineahnung2345/leetcode-cpp-practices/blob/master/46.%20Permutations.cpp

void dfs(vector<int> & prev, vector<vector<int>>& res,vector<int>&elements){
            if (elements.size()==prev.size()){
                res.push_back(prev);
            }
            else{
                for (int i : elements){
                    if (find(prev.begin(),prev.end(),i)!= prev.end()){
                        continue;
                    }
                   prev.push_back(i);
                   dfs(prev,res,elements);
                   prev.pop_back();
                }
            }
        }
