## Python

################## Python 3.13 
#### ### 

#### Python jj
### 

///  \\\ 


## python


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        mp = defaultdict(list)

        for i, v in enumerate(nums):
            mp[v].append(i)

        for pos in mp.values():
            total = sum(pos)
            left_sum = 0
            m = len(pos)

            for i in range(m):
                right_sum = total - left_sum - pos[i]

                left = pos[i] * i - left_sum
                right = right_sum - pos[i] * (m - i - 1)

                ans[pos[i]] = left + right

                left_sum += pos[i]

        return ans

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        res = 100000
        seen = {}

        for i, n in enumerate(nums):
            if n in seen:
                res = min(res, i - seen[n])
            seen[int(str(n)[::-1])] = i

        return -(res == 100000) | res
,,,

////////////////////
///
24 i have last practical on that day
///>>>>>>>>>

from collections import deque
class Solution:
     def isMaxHeap(self, arr):
          # code here
          n = len(arr)
          if n <= 1:
               return True
          
          st = deque([arr[0]])
          i = 1
          while i < n and st:
               curr = st.popleft()

               if arr[i] <= curr:
                    st.append(arr[i])
                    i += 1
               else:
                    return False
               
               if i < n:
                    if arr[i] <= curr:
                         st.append(arr[i])
                         i += 1
                    else:
                         return False
               else:
                    break
          
          return True



from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        NEG = -10**9

        prev = [[NEG] * (k + 1) for _ in range(n)]

        for i in range(m):
            curr = [[NEG] * (k + 1) for _ in range(n)]

            for j in range(n):
                gain = grid[i][j]
                need = 1 if gain > 0 else 0

                limit = min(k, i + j)

                if i == 0 and j == 0:
                    curr[0][0] = 0
                    continue

                for c in range(need, limit + 1):
                    best = NEG

                    if i > 0 and prev[j][c - need] != NEG:
                        best = max(best, prev[j][c - need] + gain)

                    if j > 0 and curr[j - 1][c - need] != NEG:
                        best = max(best, curr[j - 1][c - need] + gain)

                    curr[j][c] = best

            prev = curr

        ans = max(prev[n - 1])
        return -1 if ans < 0 else ans


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        a_sum = 0
        F = 0
        n = len(A)

        for i in range(n):
            a_sum += A[i]
            F += i * A[i]

        res = F

        for i in range(1, n):
            F += a_sum - n * A[-i]
            res = max(res, F)

        return res


