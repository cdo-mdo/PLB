def merge(intervals):
    # Sort intervals by the start time
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # If merged is empty or no overlap, add the interval to merged
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Overlapping intervals, merge them
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Example usage
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))
