class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_altitude = 0
        max_altitude = 0

        for diff in gain:
            curr_altitude += diff
            max_altitude = max(max_altitude, curr_altitude)
            

        return max_altitude


        