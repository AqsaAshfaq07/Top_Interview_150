class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            last_merged_interval = result[-1]

            if current_interval[0] <= last_merged_interval[1]:
                result[-1] = [last_merged_interval[0], max(last_merged_interval[1], current_interval[1])]
            else:
                result.append(current_interval)

        return result
