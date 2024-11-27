# Most Frequent Character

## Problem Description
Write a function, `most_frequent_char`, that takes in a string as an argument. The function should return the most frequent character of the string. If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty.

---

## Solution Approaches

### Approach 1: Using a Manual Counter
This approach involves manually counting the occurrences of each character using a dictionary.

#### Steps:
1. **Initialize a Dictionary**: Create an empty dictionary `count` to store the frequency of each character in the string.
2. **Count Frequencies**:
   - Iterate through each character in the string.
   - If the character is not in the dictionary, add it with an initial count of `0`.
   - Increment the character's count.
3. **Determine the Most Frequent Character**:
   - Traverse the string again to ensure that ties are resolved by the earliest occurrence.
   - Keep track of the "best" character that has the highest frequency so far.
4. **Return the Result**: Return the character stored in `best`.

#### Code:
```python
def most_frequent_char(s):
    # Create a dictionary to count the frequency of each character
    count = {}
    for char in s:
        # Initialize the character count if it doesn't exist
        if char not in count:
            count[char] = 0
        # Increment the character count
        count[char] += 1

    # Variable to track the most frequent character
    best = None
    for char in s:
        # Update 'best' if no character is set yet or the current character is more frequent
        if best is None or count[char] > count[best]:
            best = char
    # Return the most frequent character
    return best
```
### Complexity:
  * Time Complexity: O(n), where n is the length of the string.
  * Counting the characters: O(n).
  * Traversing the string again to find the most frequent character: O(n).
  * Space Complexity: O(n), for storing character frequencies in the dictionary.


### Approach 2: Using Python's collections.Counter
This approach simplifies the frequency counting process by utilizing the Counter class from Python's collections module.

### Steps:
1. **Count Frequencies Using Counter**: Use Counter(s) to automatically calculate the frequency of each character in the string.
2. **Find the Most Frequent Character**:
    * Iterate through the string.
    * Keep track of the character with the highest frequency seen so far.
3. **Return the Result**: Return the character with the highest frequency.
 
#### Code:
```python
from collections import Counter

def most_frequent_char(s):
    # Use Counter to calculate frequencies of each character in the string
    count = Counter(s)

    # Variable to track the most frequent character
    max_value = None
    for char in s:
        # Update 'max_value' if no character is set yet or the current character is more frequent
        if max_value is None or count[char] > count[max_value]:
            max_value = char
    # Return the most frequent character
    return max_value
```
### Complexity:
  * Time Complexity: O(n), where n is the length of the string.
  * Counter(s) processes the string in O(n).
  * Traversing the string to find the most frequent character: O(n).
  * Space Complexity: O(n), for storing character frequencies in the Counter.

### Test Cases
``` python
# Test Case 1: Multiple occurrences of 'e', tied with earlier position
print(most_frequent_char('bookeeper'))  # Output: 'e'

# Test Case 2: 'd' appears earlier in the string
print(most_frequent_char('david'))  # Output: 'd'

# Test Case 3: 'b' appears earlier than other most frequent characters
print(most_frequent_char('abby'))  # Output: 'b'

# Test Case 4: 'i' is the most frequent, despite ties
print(most_frequent_char('mississippi'))  # Output: 'i'

# Test Case 5: 'e' appears earlier and most frequently
print(most_frequent_char('eleventennine'))  # Output: 'e'

# Test Case 6: 'r' appears earlier than other most frequent characters
print(most_frequent_char('riverbed'))  # Output: 'r'
```

### Summary
Both approaches solve the problem efficiently in O(n) time complexity.

  * Approach 1 involves a manual implementation of counting and determining the most frequent character.
  * Approach 2 leverages Python's Counter for counting, making the code cleaner and more concise. Choose the approach based on preference and familiarity with Python's standard library.