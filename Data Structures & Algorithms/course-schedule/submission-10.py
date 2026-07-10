class Solution:
    from collections import defaultdict
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        maxLen = 0

        if numCourses <= 0:
            return False
        if numCourses > 0 and not prerequisites:
            return True
        
        for [c0, c1] in prerequisites:
            courses[c0].append(c1)

        def cycle(i, traversed):
            if i in courses:
                traversed.append(i)
                rez = []
                for k in courses[i]:
                    if k in traversed:
                        return False
                    rez.append(cycle(k, traversed.copy()))
                return all(rez)
            else:
                return True
        
        res = []

        for k in courses.keys():
            res.append(cycle(k, []))

        return all(res)