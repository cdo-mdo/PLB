def findMinArrowShots(points):
    if not points:
        return 0

    # short by the end of each interval
    points.sort(key=lambda x: x[1])

    arrows = 0
    end float('-inf')

    for x_start, x_end in points:
        # if the start of the balloon is greater than the end of the last arrow
        if x_start > end:
            arrow += 1
            end = x_end

    return arrows


