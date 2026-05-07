## Python
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre = [0] * n
        suf = [0] * n
        res = [0] * n

        # prefix max
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = max(pre[i - 1], nums[i])

        # suffix min
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(suf[i + 1], nums[i])

        res[-1] = pre[-1]

        # build answer
        for i in range(n - 2, -1, -1):

            # merge segment
            if pre[i] > suf[i + 1]:
                res[i] = res[i + 1]

            # new segment
            else:
                res[i] = pre[i]

        return res


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        r, c=len(box), len(box[0])
        rotate=[['.']*r for _ in range(c)]
        for i, row in enumerate(box):
            bottom=c-1
            for j in range(c-1, -1, -1):
                if row[j]=='#':
                    rotate[bottom][r-1-i]='#'
                    bottom-=1
                elif row[j]=='*':
                    rotate[j][r-1-i]='*'
                    bottom=j-1
        return rotate
        



class Solution {
  public:
    int ans;
    void solve(Node* root){
        if(!root){
            return;
        }
        solve(root->left);
        ans++;
        solve(root->right);
    }
    
    int getSize(Node* root) {
        ans = 0;
        solve(root);
        return ans;
    }
};

class Solution {
  public:
    int ans;
    void solve(Node* root){
        if(!root){
            return;
        }
        solve(root->left);
        ans++;
        solve(root->right);
    }
    
    int getSize(Node* root) {
        ans = 0;
        solve(root);
        return ans;
    }
};

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0: return head  

        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1  

        k %= length
        if k == 0: return head 

        tail.next = head  # circular

        steps = length - k
        newtail = head
        for _ in range(1, steps):
            newtail = newtail.next  

        newhead = newtail.next  
        newtail.next = None  

        return newhead

class Solution:
    def sumXOR(self, arr):
        # code here
        total = 0
        n = len(arr)

        for bit in range(32):
            count0 = 0
            for val in arr:
                if val & (1 << bit) == 0:
                    count0 += 1
            
            count1 = n - count0
            total += count0 * count1 * (1 << bit)
        
        return total


class Solution {
    public boolean isBinaryPalindrome(int n) {
        // code here
        String s=Integer.toBinaryString(n);
        int left=0,right=s.length()-1;
        while(left<=right){
            char leftChar=s.charAt(left);
            char rightChar=s.charAt(right);
            if(leftChar!=rightChar){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};

######### 
class Solution {
public:
    void rotate(vector<vector<int>>& mat) {
        int n = mat.size(), k = n - 1;
        for (int i = 0; i < n >> 1; i++)
            for (int j = i; j < k - i; j++) {
                int t = mat[i][j];
                mat[i][j] = mat[k - j][i];
                mat[k - j][i] = mat[k - i][k - j];
                mat[k - i][k - j] = mat[j][k - i];
                mat[j][k - i] = t;
            }
    }
};

class Solution {
  public:
  
    bool static comp(pair<int, int> &a, pair<int, int> &b){
        int x=__builtin_popcount(a.first);
        int y=__builtin_popcount(b.first);
        if(x>y) return true;
        else if(x==y) return a.second<b.second;
        else return false;
    }
  
    vector<int> sortBySetBitCount(vector<int>& arr) {
        // code here
        int n=arr.size();
        vector<pair<int, int>>tmp;
        for(int i=0; i<n; i++){
            tmp.push_back({arr[i], i});
        }
        sort(tmp.begin(), tmp.end(),comp);
        vector<int>ans;
        for(auto &it:tmp){
            ans.push_back(it.first);
        }
        return ans;
    }
};
/// Python


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


