## Python

class Solution {
  public:
    int optimalKeys(int n) {
        
        vector<int> dp(n + 1, 0);

        for (int i = 1; i <= n; i++) {
            dp[i] = i;
        }

        for (int i = 1; i <= n; i++) {

            for (int j = 1; j <= i - 3; j++) {

                dp[i] = max(dp[i], dp[j] * (i - j - 1));
            }
        }

        return dp[n];
    }
};

class Solution {
public:
    bool isGood(vector<int>& nums) {
        int n = nums.size() - 1;
        bitset<201> seen;
        bool dup = 0;

        for (auto& num : nums) {
            if (num > n) return false;

            if (seen.test(num)) {
                if (num < n || dup) return false;
                dup |= 1;
                continue;
            }

            seen.set(num);
        }

        return true;
    }
};

class Solution {
  public:
  
    void computeLPSArray(vector<int>& pat, vector<int>& lps) {
        
        int m = pat.size();

        for (int i = 1; i < m; i++) {
            
            int j = lps[i - 1];

            while (j > 0 && pat[i] != pat[j]) {
                j = lps[j - 1];
            }

            if (pat[i] == pat[j]) {
                j++;
            }

            lps[i] = j;
        }
    }

    vector<int> search(vector<int> &a, vector<int> &b) {
        
        int n = a.size();
        int m = b.size();

        vector<int> lps(m, 0);
        computeLPSArray(b, lps);

        vector<int> ans;

        int j = 0;

        for (int i = 0; i < n; i++) {

            while (j > 0 && a[i] != b[j]) {
                j = lps[j - 1];
            }

            if (a[i] == b[j]) {
                j++;
            }

            if (j == m) {
                ans.push_back(i - m + 1);
                j = lps[j - 1];
            }
        }

        return ans;
    }
};

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        seen = set()
        dup = False

        for num in nums:
            if num > n: return False

            if num in seen:
                if num < n or dup: return False
                dup = True
                continue

            seen.add(num)

        return True

class Solution {
  public:
    
    void dfs(int node, vector<vector<int>>& adj, vector<int>& visited) {
        visited[node] = 1;
        
        for (int neighbor : adj[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor, adj, visited);
            }
        }
    }

    int findMotherVertex(int V, vector<vector<int>>& edges) {
        
        vector<vector<int>> adj(V);
        
        for (auto &edge : edges) {
            adj[edge[0]].push_back(edge[1]);
        }

        vector<int> visited(V, 0);
        
        int candidate = -1;

        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                dfs(i, adj, visited);
                
                candidate = i;
            }
        }

        fill(visited.begin(), visited.end(), 0);

        dfs(candidate, adj, visited);

        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                return -1;
            }
        }

        return candidate;
    }
};


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        delta = [0] * (2 * limit + 2)

        for i in range(n // 2):
            mini = min(nums[i], nums[-1 - i])
            maxi = max(nums[i], nums[-1 - i])

            delta[2] += 2
            delta[mini + 1] -= 1
            delta[mini + maxi] -= 1
            delta[mini + maxi + 1] += 1
            delta[maxi + limit + 1] += 1

        res = n
        moves = 0

        for targ in range(2, 2 * limit + 1):
            moves += delta[targ]
            res = min(res, moves)

        return res


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        delta = [0] * (2 * limit + 2)

        for i in range(n // 2):
            mini = min(nums[i], nums[-1 - i])
            maxi = max(nums[i], nums[-1 - i])

            delta[2] += 2
            delta[mini + 1] -= 1
            delta[mini + maxi] -= 1
            delta[mini + maxi + 1] += 1
            delta[maxi + limit + 1] += 1

        res = n
        moves = 0

        for targ in range(2, 2 * limit + 1):
            moves += delta[targ]
            res = min(res, moves)

        return res


class Solution:
    def maximumJumps(self, nums, target):

        n = len(nums)

        # dp[i] stores maximum jumps to reach index i
        dp = [-1] * n

        # Starting index needs 0 jumps
        dp[0] = 0

        for i in range(1, n):

            # Check all previous indices
            for j in range(i):

                # Valid jump and previous index reachable
                if abs(nums[i] - nums[j]) <= target and dp[j] != -1:

                    # Update maximum jumps
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[-1]

class Solution {
  public:
    int maxProfit(int x, int y, vector<int> &a, vector<int> &b) {
        // code here
        int n = a.size();
        vector<pair<int,int>>vec;
        for(int i = 0 ;i<n ; i++){
            vec.push_back({a[i] - b[i] , i});
        }
        sort(vec.begin() , vec.end() , greater());
        int res = 0 , i=0;
        for(;i<x ; i++){
            if(vec[i].first<0 && n-i <=y)break;
            res+= a[vec[i].second];
        }
        for(;i<n ; i++)res+= b[vec[i].second];
        
        return res;
    }
};



class Solution {
public:
    vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {
        int T = 0, L = 0;
        int B = grid.size() - 1, R = grid[0].size() - 1;

        while (T < B && L < R) {
            int len = B - T, wid = R - L;
            int perimeter = 2 * len + 2 * wid;
            int r = k % perimeter;

            while (r--) {
                int tmp = grid[T][L];

                for (int i = L; i < R; i++)
                    grid[T][i] = grid[T][i + 1];

                for (int i = T; i < B; i++)
                    grid[i][R] = grid[i + 1][R];

                for (int i = R; i > L; i--)
                    grid[B][i] = grid[B][i - 1];

                for (int i = B; i > T; i--)
                    grid[i][L] = grid[i - 1][L];

                grid[T + 1][L] = tmp;
            }

            T++; L++;
            B--; R--;
        }

        return grid;
    }
};

class Solution {
  public:
  
    long long determinant(vector<vector<double>>& mat, int size) {
        
        double det = 1;
        
        for (int i = 0; i < size; i++) {
            
            int pivot = i;
            
            for (int j = i; j < size; j++) {
                if (abs(mat[j][i]) > 1e-9) {
                    pivot = j;
                    break;
                }
            }
            
            if (abs(mat[pivot][i]) < 1e-9)
                return 0;
            
            if (pivot != i) {
                swap(mat[pivot], mat[i]);
                det *= -1;
            }
            
            det *= mat[i][i];
            
            for (int j = i + 1; j < size; j++) {
                
                double factor = mat[j][i] / mat[i][i];
                
                for (int k = i; k < size; k++) {
                    mat[j][k] -= factor * mat[i][k];
                }
            }
        }
        
        return round(det);
    }
  
    int countSpanTree(int n, vector<vector<int>>& edges) {
        
        if (n == 1)
            return 1;
        
        vector<vector<double>> lap(n, vector<double>(n, 0));
        
        for (auto &e : edges) {
            
            int u = e[0];
            int v = e[1];
            
            lap[u][u]++;
            lap[v][v]++;
            
            lap[u][v]--;
            lap[v][u]--;
        }
        
        vector<vector<double>> cof(n - 1, vector<double>(n - 1));
        
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1; j++) {
                cof[i][j] = lap[i][j];
            }
        }
        
        return determinant(cof, n - 1);
    }
};

class Solution:
    N = 10**6 + 5
    prime = [True] * N
    prime[0] = prime[1] = False
    
    for i in range(2, 1001):
        if prime[i]:
            for j in range(i * i, N, i):
                prime[j] = False

    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        limit = nums[0]
        for c in nums:
            limit = max(limit, c)

        head = [-1] * (limit + 1)
        nxt = [-1] * n
        for i in range(n):
            val = nums[i]
            nxt[i] = head[val]
            head[val] = i

        dp = [-1] * n
        dp[0] = 0
        queue = deque([0])
        seen = set()

        while queue:
            dq = queue.popleft()

            if dq == n - 1:
                return dp[dq]

            right = dq + 1
            if right < n and dp[right] == -1:
                dp[right] = dp[dq] + 1
                queue.append(right)

            left = dq - 1
            if left >= 0 and dp[left] == -1:
                dp[left] = dp[dq] + 1
                queue.append(left)

            val = nums[dq]
            if Solution.prime[val] and val not in seen:
                seen.add(val)
                for i in range(val, limit + 1, val):
                    j = head[i]
                    while j != -1:
                        if dp[j] == -1:
                            dp[j] = dp[dq] + 1
                            queue.append(j)
                        j = nxt[j]
                    head[i] = -1
        return -1


class Solution {
public:
    
    bool check(string &t) {
        int bal = 0;
        
        for(char c : t) {
            if(c == '('){
                bal++;
            }
            else if(c == ')'){
                bal--;
                if(bal < 0){
                    return false;
                }
            }
        }
        
        return bal == 0;
    }
    
    vector<string> validParenthesis(string &s) {
        
        unordered_set<string> vis;
        queue<string> q;
        vector<string> ans;
        
        q.push(s);
        vis.insert(s);
        
        bool found = false;
        
        while(!q.empty()){
            
            string cur = q.front();
            q.pop();
            
            if(check(cur)) {
                ans.push_back(cur);
                found = true;
            }
            
            if(found){
                continue;
            }
            
            for(int i = 0; i < cur.size(); i++) {
                
                if(cur[i] != '(' && cur[i] != ')'){
                    continue;
                }
                
                string nxt = cur.substr(0, i) + cur.substr(i + 1);
                
                if(!vis.count(nxt)) {
                    vis.insert(nxt);
                    q.push(nxt);
                }
            }
        }
        
        sort(ans.begin(), ans.end());
        ans.erase(unique(ans.begin(), ans.end()), ans.end());
        
        return ans;
    }
};

*
Definition for Node
struct Node
{
    int data;
    Node* left;
    Node* right;

    Node(int x){
        data = x;
        left = right = nullptr;
    }
};
*/

class Solution {
    string solve(Node* root){
        if (!root) return "N|";
        string ans = "";
        ans += to_string(root->data) + "|";
        ans += solve(root->left);
        ans += solve(root->right);
        return ans;
    }
  public:
    bool isSubTree(Node *root1, Node *root2) {
        // code here
        string pre1 = solve(root1);
        string pre2 = solve(root2);
        if (pre1.find(pre2)!=string::npos) return true;
        return false;
    }
};

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


