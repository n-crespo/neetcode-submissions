"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort the input
        intervals.sort(key = lambda i : i.start)
        last_end = 0

        for interval in intervals:
            start_time = interval.start
            end_time = interval.end

            if start_time < last_end:
                return False
            last_end = end_time
            
        return True
