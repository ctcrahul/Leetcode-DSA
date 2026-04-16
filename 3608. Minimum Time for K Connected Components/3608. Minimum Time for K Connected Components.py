class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, x, y):
            px,py = find(parent,x), find(parent,y)
            if px!= py:
                parent[px] = py
                return True
            return False

        def count(time):
            parent = list(range(n))
            components = n
            for u,v,t in edges:
                if t > time:
                    if union(parent,u,v):
                        components-=1
            return components

        if count(-1) >= k:
            return 0

        times = sorted(set(edge[2] for edge in edges))
        left = 0
        right = len(times)-1
        answer = times[-1]
        while(left <= right):
            mid = (left + right)//2
            current_time = times[mid]
            if count(current_time) >= k:
                answer = current_time
                right = mid -1 
            else:
                left = mid + 1
        return answer
                
