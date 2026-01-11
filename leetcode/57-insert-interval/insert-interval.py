class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)

        new_list = list()

        i = 0

        while i < n and intervals[i][1] < newInterval[0]:
            new_list.append(intervals[i])
            i += 1


        new_start = newInterval[0]
        new_end = newInterval[1]

        while i < n and new_end >= intervals[i][0]:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1

        new_list.append([new_start, new_end])
        print(new_list)

        while i < n:
            new_list.append(intervals[i])
            i += 1

        return new_list

        