# Sort Characters By Frequency
# Bucket Sort Solution:
from collections import Counter, defaultdict
from typing import List

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        buckets = defaultdict(list)

        for char, freq in count.items():
            buckets[freq].append(char)

        res = []
        for i in range(len(s), 0, -1):
            if i in buckets:
                for c in buckets[i]:
                    res.append(c * i)

        return "".join(res)
    
# Time Complexity: O(n), where n is the length of the string s. We count the frequency of each character and then build the result string.
# Space Complexity: O(n), as we use additional space to store the frequency count and the buckets.
# This bucket sort solution efficiently groups characters by their frequencies and constructs the sorted string in a single pass through the buckets.


# Test Cases
sol = Solution()

# Test Case 1:
s1 = "tree"
print(sol.frequencySort(s1))  # Expected output: "eert"

# Test Case 2:
s2 = "cccaaa"
print(sol.frequencySort(s2))  # Expected output: "aaaccc"

# Test Case 3:
s3 = "Aabb"
print(sol.frequencySort(s3))  # Expected output: "bbAa"
