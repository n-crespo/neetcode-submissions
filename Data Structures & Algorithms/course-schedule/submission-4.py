class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # course: prerequisites
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []

        for course, prereq in prerequisites:
            preMap[course].append(prereq)


        visiting = set()
        def dfs(course):
            if course in visiting:
                # cycle in DFS path!
                return False
            
            if preMap[course] == []:
                # this course has no prereqs
                return True
            
            # mark this course as in our path
            visiting.add(course)
            for prereq in preMap[course]:
                # go through all prereqs and check!
                possible = dfs(prereq)
                # if any prerequisite is impossible, this course is impossible to take
                if not possible: return False

            # this course is possible to take
            visiting.remove(course)
            # remove prerequisites so we avoid doing this computation again later!
            preMap[course] = []

            # this is possible!
            return True
        

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True