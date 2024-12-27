class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total_tank = 0
        curr_tank = 0
        start_station = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            # if we run out of gas at this station
            if curr_tank < 0:
                start_station = i + 1 # start from the next station
                curr_tank = 0;

        # Check if we have enough gas in overall
        return start_station if total_tank >= 0 else -1

solution = Solution()
print(solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
