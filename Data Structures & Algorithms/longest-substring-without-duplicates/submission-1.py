class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #init a map to keep track of the last index

        mp = {}

         #init first index
        fi = 0
         #init result to keep track of the longest str
        res  = 0

         #loop right index in s

        for r in range(len(s)):
            #if s[r] in mp, move fi forward but not backward
            if s[r] in mp:
                fi = max(mp[s[r]]+1, fi)
                #assign mp[s[r]] to r index

            mp[s[r]]=r

                #assing resutl to the longest length

            res = max(res, r - fi +1)
        return res

            


