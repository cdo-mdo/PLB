class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if (len(nums) <= 1):
            return True
        farthest = 0
        for i in range(len(nums)):
            if (i > farthest):
                return False
            farthest = max(farthest, i + nums[i])
            if (farthest >= len(nums) - 1):
                return True
        return False

solution = Solution()
print(solution.canJump([2, 3, 1, 1, 4]))
