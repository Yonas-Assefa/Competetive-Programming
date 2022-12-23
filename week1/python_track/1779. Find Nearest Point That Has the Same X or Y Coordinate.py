class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid_point_index = -1
        distance = float("inf")
        points_len = len(points)
        for i in range(points_len):
            if points[i][0] == x or points[i][1] == y:
                current_distance = abs(x - points[i][0]) + abs(y - points[i][1])
                if current_distance < distance:
                    distance = current_distance
                    valid_point_index = i
                elif current_distance == distance:
                    valid_point_index = min(valid_point_index , i)
        return valid_point_index
                    
