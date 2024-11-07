#!/usr/bin/python3

def find_combinations(nums, target):
    result = []

    def backtrack(start, current_combination, current_sum):
        # If the current sum matches the target, add it to the results
        if current_sum == target:
            result.append(current_combination[:])
            return
        
        # If the current sum exceeds the target, we stop exploring this path
        if current_sum > target:
            return

        # Try each number in nums starting from 'start' to avoid duplicate combinations
        for i in range(start, len(nums)):
            # Add nums[i] to the combination
            current_combination.append(nums[i])

            # Recur with updated sum and current combination
            backtrack(i, current_combination, current_sum + nums[i])

            # Remove nums[i] to backtrack
            print(current_combination)
            current_combination.pop()

    # Start backtracking with an empty combination and 0 sum
    backtrack(0, [], 0)
    return result

# Example usage
nums = [2, 3, 6, 7]
target = 7
print(find_combinations(nums, target))
