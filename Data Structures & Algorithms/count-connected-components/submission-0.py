class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            result = n1 # node

            # stop searching whe node itself is its own parent
            while result != parents[result]:
                parents[result] = parents[parents[result]]
                result = parents[result]

            return result
        
        def union(n1, n2): 
            # get the parents of these nodes
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                # choose larger rank as parents
                parents[p1] = p2
                rank[p2] += rank[p1]
            else:
                parents[p2] = p1
                rank[p1] += rank[p2]
            return 1

        result = n
        for n1, n2 in edges:
            result -= union(n1, n2)
        return result




        