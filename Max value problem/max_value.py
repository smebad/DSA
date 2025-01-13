#  Max value

# Solution:

def max_value(nums): 
  max_num = float('-inf') # Step 1: Starting with the smallest possible value (negative infinity)

  for num in nums: # Step 2: Loop through each number in the list
    if num > max_num: # Step 3: Check if the current number is larger than max_num
      max_num = num # Step 4: If yes, update max_num

  return max_num # Step 5: After the loop, return the largest number found

  # Test cases
if __name__ == "__main__":
    test_list = [3, 1, 4, 1, 5, 9]
    print(f"Max value in {test_list}: {max_value(test_list)}")  # Expected: 9

    test_list2 = [-10, -20, -30, -5]
    print(f"Max value in {test_list2}: {max_value(test_list2)}")  # Expected: -5

    test_list3 = [7]
    print(f"Max value in {test_list3}: {max_value(test_list3)}")  # Expected: 7

    test_list4 = []
    print(f"Max value in {test_list4}: {max_value(test_list4)}")  # Expected: float('-inf')

  