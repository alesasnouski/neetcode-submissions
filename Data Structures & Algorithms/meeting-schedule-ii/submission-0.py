"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        def register_in_room(interval):
            for r, room in enumerate(rooms):
                for iv in room:
                    if interval[0] < iv[1]:
                        break  # room doesn't fit
                else:
                    room.append(interval)
                    rooms[r] = sorted(room)
                    break
            else:
                rooms.append([interval])

        intervals = sorted([(ivl.start, ivl.end) for ivl in intervals])
        for i in range(0, len(intervals)):
            register_in_room(intervals[i])
        return len(rooms)