# Is Prime Problem

## Problem Description
Write a function, `is_prime`, that takes a positive integer `num` as an argument and returns a boolean indicating whether the number is prime. A prime number is a number greater than 1 that is only divisible by 1 and itself.

---

## Solution

The function checks if the number is less than 2 (in which case it is not prime). Then, it iterates from 2 to `num - 1` to check for divisibility. If any divisor is found, the function returns `False`; otherwise, it returns `True`.

### Code Implementation
```python
def is_prime(num):
    if num < 2:
        return False  # Numbers less than 2 are not prime

    for i in range(2, num):  # Check divisibility from 2 to num - 1
        if num % i == 0:  # If divisible, it's not prime
            return False

    return True  # The number is prime
```
### Example Test Cases
``` python
print("Test Case 1: is_prime(2) ->", is_prime(2))        # Expected: True
print("Test Case 2: is_prime(3) ->", is_prime(3))        # Expected: True
print("Test Case 3: is_prime(4) ->", is_prime(4))        # Expected: False
print("Test Case 4: is_prime(5) ->", is_prime(5))        # Expected: True
print("Test Case 5: is_prime(6) ->", is_prime(6))        # Expected: False
print("Test Case 6: is_prime(7) ->", is_prime(7))        # Expected: True
print("Test Case 7: is_prime(8) ->", is_prime(8))        # Expected: False
print("Test Case 8: is_prime(25) ->", is_prime(25))      # Expected: False
print("Test Case 9: is_prime(31) ->", is_prime(31))      # Expected: True
print("Test Case 10: is_prime(2017) ->", is_prime(2017)) # Expected: True
print("Test Case 11: is_prime(2048) ->", is_prime(2048)) # Expected: False
print("Test Case 12: is_prime(1) ->", is_prime(1))       # Expected: False
print("Test Case 13: is_prime(713) ->", is_prime(713))   # Expected: False
```
### Expected Output
```
Test Case 1: is_prime(2) -> True
Test Case 2: is_prime(3) -> True
Test Case 3: is_prime(4) -> False
Test Case 4: is_prime(5) -> True
Test Case 5: is_prime(6) -> False
Test Case 6: is_prime(7) -> True
Test Case 7: is_prime(8) -> False
Test Case 8: is_prime(25) -> False
Test Case 9: is_prime(31) -> True
Test Case 10: is_prime(2017) -> True
Test Case 11: is_prime(2048) -> False
Test Case 12: is_prime(1) -> False
Test Case 13: is_prime(713) -> False
```
