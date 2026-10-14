class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            result = n1 # node

            # climb up the tree until we find a node that is
            # its own parent. that is the root/highest parent
            while result != parent[result]:
                parent[result] = parent[parent[result]]
                result = parent[result]

            return result
        
        def union(n1, n2): 
            # get the parent of these nodes
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                # choose larger rank as parent
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1

        result = n
        for n1, n2 in edges:
            result -= union(n1, n2)
        return result




        