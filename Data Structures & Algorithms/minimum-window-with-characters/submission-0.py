from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        window = Counter()

        have, need = 0, len(t_count)
        res = ""
        min_len = float("inf")
        l = 0  # <--- Added missing left pointer initialization

        for r, c in enumerate(s):
            window[c] += 1

            if c in t_count and window[c] == t_count[c]:
                have += 1

            # Try shrinking window from left while it remains valid
            while have == need:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    res = s[l : r + 1]

                # Remove left character
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                
                l += 1

        return res
        