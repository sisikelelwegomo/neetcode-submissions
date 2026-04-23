class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        count = {}
        fi = 0
        maxf = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - fi + 1) - maxf > k:
                count[s[fi]] -= 1
                fi += 1
            res = max(res, r-fi+1)
        return res
        