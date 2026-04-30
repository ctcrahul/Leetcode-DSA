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
