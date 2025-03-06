class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # By always shooting at the xend of an active group of overlapping balloons, we         minimize the number of arrows required.
        points.sort(key= lambda point:point[1])
        arrow = 1
        end = points[0][1]
        for point in points:
            if point[0] > end:
                arrow += 1
                end = point[1]
        return arrow
