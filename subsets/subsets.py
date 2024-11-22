def subsets(nums):
    def backtrack(start, path):
        # Add the current subset
        result.append(path[:])
        # explore further subset
        for i in range(start, len(nums)):
            # Include num[i]
            path.append(nums[i])
            # Recurse
            backtrack(i + 1, path)
            # Backtrack: remove nums[i]
            path.pop()

    result = []
    backtrack(0, [])
    return result

def subsets1(nums):
    result = [[]]
    for num in nums:
        result += [curr + [num] for curr in result]
    return result    


# Example usage
print(subsets([1, 2, 3]))
print(subsets1([1, 2, 3]))
print(subsets1([1, 2, 3, 4]))
