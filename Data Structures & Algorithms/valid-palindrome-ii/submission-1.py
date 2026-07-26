class Solution:
    def validPalindrome(self, s: str) -> bool:

        def helper_function(l:int,r:int)->bool:

            while l<r:
                if s[l]!=s[r]:
                    return False

                l+=1
                r-=1
            return True

        left=0
        right=len(s)-1

        while left<right:
            if s[left]!=s[right]:
                return helper_function(left+1,right) or helper_function(left,right-1)
            left+=1
            right-=1
        return True



               

        