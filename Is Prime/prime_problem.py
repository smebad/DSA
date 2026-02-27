# Is Prime
def is_prime(num): 
  if num < 2:
     return False # Step 1: Checking if the number is less than 2

  for i in range(2, num): # Step 2: Looping from 2 to num - 1
    if num % i == 0:  # Step 3: Checking if num is divisible by i
      return False # Step 4: If divisible, return False

  return True # Step 5: If not divisible, return True

# Test Cases
if __name__ == "__main__":
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
