"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def doesOverlap(self, endTime1, startTime2):
        return endTime1 > startTime2
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def sortByEndTime(int1, int2):
            return int1[1] > int2[1]
        intervals.sort(key=lambda x: x.end)

        for i in range(0, len(intervals) - 1):
            if self.doesOverlap(intervals[i].end, intervals[i + 1].start):
                return False
        return True