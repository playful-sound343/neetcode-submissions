from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Create a hash map where values default to empty lists
        anagram_map = defaultdict(list)
        
        # 2. Iterate through each string in the input
        for s in strs:
            # Sort the characters of s and join them back into a string
            # sorted("eat") -> ['a', 'e', 't'] -> joined to "aet"
            sorted_s = "".join(sorted(s))
            
            # 3. Add the original string s to its corresponding anagram group
            anagram_map[sorted_s].append(s)
            
        # 4. Return all the groups as a list of lists
        return list(anagram_map.values())



