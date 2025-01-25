class Solution {
public:
    bool isPalindrome(int x) {
        int dup = x;
        long long revNum = 0;
        while(dup > 0){
            int digit = dup % 10;
            revNum  = (revNum * 10) + digit;
            dup = dup / 10;
        }
        if(revNum == x){
            return true;
        }
        else{
            return false;
        }
    }
};