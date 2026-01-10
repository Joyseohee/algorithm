from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_map = Counter(s)

        odd, even = 0, 0
        is_odd = False

        for k, v in count_map.items():
            if v % 2 == 0:
                even += v
            else:
                odd += (v - 1)

                is_odd = True

        return even + odd + 1 if is_odd else even
        