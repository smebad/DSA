# Divide Players Into Teams of Equal Skill - LeetCode

## Problem Overview

The problem **Divide Players Into Teams of Equal Skill** asks us to divide an even number of players into teams of size 2 such that **each team has the same total skill**.

Each player has a positive integer skill value, and:

* Every player must belong to exactly one team
* All teams must have the same total skill
* The *chemistry* of a team is defined as the product of the two players' skills

If such a division is possible, we return the **sum of the chemistry of all teams**. Otherwise, we return `-1`.

---

## Key Insight

If there are `n` players, then:

* We must form `n / 2` teams
* Each team must have the same total skill

Let:

* `total = sum(skill)`

Then the required total skill per team is:

```
team_sum = (2 * total) / n
```

If this value is not an integer, forming valid teams is impossible.

---

## Provided Solution (With Comments)

```python
from typing import List
from collections import Counter

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Calculate total skill of all players
        total = sum(skill)

        # If team sum is not an integer, return -1
        if (2 * total) % len(skill):
            return -1
        
        # Count frequency of each skill value
        count = Counter(skill)
        
        # Target total skill per team
        target = (2 * total) // len(skill)
        
        res = 0  # Stores total chemistry

        # Try pairing each player
        for s in skill:
            # Skip if this skill value has already been used
            if not count[s]:
                continue
            
            # Use one player with skill s
            count[s] -= 1
            diff = target - s  # Required partner skill

            # If no matching partner exists, return -1
            if not count[diff]:
                return -1
            
            # Add chemistry of this pair
            res += s * diff

            # Use one player with skill diff
            count[diff] -= 1
        
        return res
```

---

## Approach and Logic Explained Simply

### Step 1: Determine Required Team Skill

If players can be divided correctly, then every team must have the same total skill. We compute this value first. If it is not an integer, we immediately return `-1`.

### Step 2: Count Skill Frequencies

We use a `Counter` to track how many players have each skill. This allows us to efficiently find and remove matching players.

### Step 3: Pair Players Greedily

For each skill value `s`:

* We try to find another player with skill `target - s`
* If such a player exists, we form a team
* If not, a valid division is impossible

Each successful pairing adds `s * (target - s)` to the total chemistry.

### Step 4: Return the Result

If all players are paired successfully, return the accumulated chemistry. Otherwise, return `-1`.

---

## Why This Works

* Every valid team must sum to the same value
* Pairing a skill `s` with `target - s` ensures this condition
* Using a frequency map prevents reusing players

This guarantees correctness while remaining efficient.

---

## Time and Space Complexity

### Time Complexity

```
O(n)
```

* Each player is processed once
* All operations inside the loop are constant time

### Space Complexity

```
O(k)
```

* `k` is the number of unique skill values
* This is due to the `Counter` used for frequency tracking

---

## Most Optimal Solution

This solution is optimal because:

* It avoids sorting, which would cost `O(n log n)`
* It uses a single pass with constant-time lookups
* It efficiently handles large inputs within constraints

A sorting-based approach would be simpler conceptually, but slower for large inputs. This frequency-based greedy solution provides the best balance of speed and clarity.

---

## Example

Input:

```
skill = [3,2,5,1,3,4]
```

Teams formed:

* (1, 5)
* (2, 4)
* (3, 3)

Chemistry sum:

```
1*5 + 2*4 + 3*3 = 22
```

Output:

```
22
```

---

## Test Cases
```python
solution = Solution()
skill1 = [3,2,5,1,3,4]
print(solution.dividePlayers(skill1))  # Output: 22

skill2 = [3,4]
print(solution.dividePlayers(skill2))  # Output: 12

skill3 = [1,1,2,3]
print(solution.dividePlayers(skill3))  # Output: -1
```
