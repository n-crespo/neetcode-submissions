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
            
            visiting.add(course)
            for prereq in preMap[course]:
                possible = dfs(prereq)
                if not possible: return False

            visiting.remove(course)
            preMap[course] = []
            return True
        

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True