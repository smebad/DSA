# Design Parking System
# Array Solution:
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.spaces[carType - 1] > 0:
            self.spaces[carType - 1] -= 1
            return True
        return False
    
# Time Complexity: O(1) for both initialization and addCar method.
# Space Complexity: O(1) since we are using a fixed-size array to store the parking spaces.
# This array solution is efficient and straightforward for the given problem constraints.


# Test Cases:
# Test Case1:
sol = ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
args = [[1, 1, 0], [1], [2], [3], [1]]
obj = ParkingSystem(*args[0])
print(obj.addCar(*args[1]))  # Output: True
print(obj.addCar(*args[2]))  # Output: True
print(obj.addCar(*args[3]))  # Output: False
print(obj.addCar(*args[4]))  # Output: False
