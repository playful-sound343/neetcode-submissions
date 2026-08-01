from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=defaultdict(int)
        left=0
        ans=0
        max_freq=0

        for right,ch in enumerate(s):
            freq[ch]+=1

            max_freq=max(max_freq,freq[ch])

            while (right-left+1)-max_freq>k:
                freq[left]-=1
                left+=1

            ans=max(ans,right-left+1)

        return ans



        

        