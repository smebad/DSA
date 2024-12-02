# Pair Product

## Problem Statement
The **pair product** problem involves finding two indices in a list such that the elements at those indices multiply to a given target product. The indices returned must be unique. 

The function takes two arguments:
- A list of numbers.
- A target product.

The output is a tuple containing the pair of indices whose elements multiply to the target product. There is a guarantee that one such pair exists.

---

## Approach

### Key Insight
The problem can be solved efficiently using a **hash map (dictionary)** to store numbers encountered so far along with their indices. This allows us to quickly check if the complement (the other number needed to reach the target product) exists.

### Steps to Solve
1. Iterate through the list.
2. For each number, calculate its complement using the formula:
   \[
   \text{complement} = \frac{\text{target product}}{\text{current number}}
   \]
3. Check if the complement exists in the hash map. If it does, return the current index and the index of the complement.
4. Otherwise, store the current number and its index in the hash map for future reference.

This approach ensures that we only traverse the list once and perform constant-time lookups, resulting in a time complexity of \( O(n) \).

---

## Solution Code

```python
def pair_product(numbers, target_product):
    """
    Finds a pair of indices in the list whose elements multiply to the target product.

    Args:
    - numbers (list): List of integers.
    - target_product (int): Target product to achieve.

    Returns:
    - tuple: A pair of indices (i, j) such that numbers[i] * numbers[j] == target_product.
    """
    # Dictionary to store numbers and their indices
    previous_nums = {}
    
    # Iterate through the list
    for index, num in enumerate(numbers):
        # Calculate the complement
        complement = target_product / num
        
        # Check if the complement is already in the dictionary
        if complement in previous_nums:
            # Return the current index and the index of the complement
            return (index, previous_nums[complement])
        
        # Otherwise, store the current number with its index
        previous_nums[num] = index
```
```python
# Test cases
print(pair_product([3, 2, 5, 4, 1], 8))    # -> (1, 3)
print(pair_product([3, 2, 5, 4, 1], 10))   # -> (1, 2)
print(pair_product([4, 7, 9, 2, 5, 1], 35)) # -> (1, 4)
print(pair_product([4, 6, 8, 2], 16))      # -> (2, 3)

# Large input test case
numbers = [i for i in range(1, 6001)]
print(pair_product(numbers, 35994000))     # -> (5998, 5999)
```
## Time Complexity
* Time Complexity: O(n)
    * The function iterates through the list once, and dictionary lookups are O(1) on average.
* Space Complexity: On
    * A hash map is used to store numbers and their indices, which takes linear space relative to the input size.

## Summary
The pair_product function provides an efficient solution to find the pair of indices whose elements multiply to a given target product. The use of a hash map ensures linear time complexity while keeping the code clean and simple.