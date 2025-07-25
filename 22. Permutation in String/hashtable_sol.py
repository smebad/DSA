# Permutation in String
# Hashtable solution:
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        
        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
        return False
    
# Time complexity: O(n * m), where n is the length of s2 and m is the length of s1.
# Space complexity: O(1), since the size of the hashtable is limited to the number of unique characters in s1 and s2.
# This is a hashtable solution that uses a sliding window approach to check for permutations of s1 in s2. But it is not the most efficient solution.


# Test Cases:
# Test Case 1
print(Solution().checkInclusion('ab', 'eidbaooo')) # True

# Test Case 2
print(Solution().checkInclusion('ab', 'eidboaoo')) # False
