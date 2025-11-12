# Design Parking System - LeetCode

## Problem Description

The "Design Parking System" problem asks you to create a class for a parking lot with three types of spaces: big, medium, and small. Each type has a fixed number of parking slots. You need to implement a system that:

1. Initializes the parking lot with a specific number of slots for each type.
2. Allows cars to park based on their type (big = 1, medium = 2, small = 3).
3. Returns `True` if a car can park in an available slot or `False` if no slot is available.

### Example

```
Input:
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output:
[null, true, true, false, false]
```

Explanation:

```
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // true (1 big slot available)
parkingSystem.addCar(2); // true (1 medium slot available)
parkingSystem.addCar(3); // false (no small slot available)
parkingSystem.addCar(1); // false (big slot already taken)
```

## Solution Code with Comments

```python
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        # Store available parking spaces for each type in a list
        # Index 0: big, Index 1: medium, Index 2: small
        self.spaces = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        # Check if there is an available slot for the given car type
        if self.spaces[carType - 1] > 0:
            # Reduce the available count as the car parks
            self.spaces[carType - 1] -= 1
            return True
        # No slot available, cannot park the car
        return False
```

## Approach and Logic

* Use a fixed-size array to store available parking slots for each type.
* When a car wants to park:

  * Check if there is an available slot for its type.
  * If available, decrement the count for that type and return `True`.
  * Otherwise, return `False`.
* The `carType - 1` mapping is used because arrays are 0-indexed.

### Why this approach works

* Simple and efficient because the number of car types is fixed (3 types).
* Each parking check is a constant-time operation.
* No need for complex data structures since the problem constraints are small and fixed.

## Time and Space Complexity

* **Time Complexity**:

  * `__init__`: O(1) — initialization of a fixed-size array.
  * `addCar`: O(1) — single check and update operation.
* **Space Complexity**: O(1) — fixed-size array of length 3.

## Test Cases

```python
# Initialize parking system
obj = ParkingSystem(1, 1, 0)

# Test Case 1: Add a big car
print(obj.addCar(1))  # True

# Test Case 2: Add a medium car
print(obj.addCar(2))  # True

# Test Case 3: Add a small car
print(obj.addCar(3))  # False (no small slot)

# Test Case 4: Add another big car
print(obj.addCar(1))  # False (big slot already taken)
```