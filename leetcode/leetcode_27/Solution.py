def removeElement(nums, val):
    slow = 0; # pointer to track the position to overwrite
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1

    return slow        

nums = [3, 2, 2, 3]
removeElement(nums, 3)
print(nums)
