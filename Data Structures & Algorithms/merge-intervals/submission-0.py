class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort the list in ascending orders based on their start values
        sorted_intervals = sorted(intervals)
        no_overlap = [sorted_intervals[0]]

        # determine how 2 intervals overlap
        for start, end in sorted_intervals[1:]:
            latest_end = no_overlap[-1][1]

            if start <= latest_end:
                no_overlap[-1][1] = max(end, latest_end)
            else:
                no_overlap.append([start,end])

        return no_overlap
 

        