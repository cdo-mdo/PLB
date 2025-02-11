def merge(nums1, m, nums2, n):
    # Pointers for nums1, nums2 and merged array
    p1, p2, p = m - 1, n - 1, m + n - 1

    # Merge the arrays starting from the largest value
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # If there are remaining elements in nums2, copy them
    nums1[:p2 + 1] = nums2[:p2 + 1]

