# Permutation in String
# Sliding Window solution:
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
    
# Time complexity: O(n), where n is the length of s2. This is because we are iterating through s2 once and updating the counts in constant time.
# Space complexity: O(1), since the size of the count arrays is fixed at 26 (for each letter in the alphabet).
# This is a sliding window solution that uses two pointers to check for permutations of s1 in s2. It is more efficient than the hashtable solution.


# Test Cases:
# Test Case 1
print(Solution().checkInclusion('ab', 'eidbaooo')) # True

# Test Case 2
print(Solution().checkInclusion('ab', 'eidboaoo')) # False
