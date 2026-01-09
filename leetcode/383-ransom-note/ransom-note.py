from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = Counter(magazine)
        for c in ransomNote:
            if counts[c] > 0:
                counts[c] -= 1

            else:
                return False


        return True
        
        