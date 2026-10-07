class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    #    create/expand the window -> check for validity -> Shrink -> Record
            result = 0 
            l = 0
            hashSet = {i: 0 for i in s}
            for r in range(len(s)):
                hashSet[s[r]] = hashSet.get(s[r], 0) + 1

                while (r - l + 1) - max(hashSet.values()) > k:
                    hashSet[s[l]] = hashSet.get(s[l]) - 1 
                    l += 1
                    

                result = max(result, r - l + 1)
            return result
