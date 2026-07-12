AI
⬇️
Machine Learning
⬇️
Deep Learning
⬇️
Generative AI
⬇️
LLMs




...

class Solution {
  public:
    int maxAmount(vector<int>& arr, int k) {
        const int MOD = 1000000007;

        priority_queue<int> pq;

        for (int x : arr)
            if (x > 0)
                pq.push(x);

        long long ans = 0;

        while (k-- && !pq.empty()) {

            int cur = pq.top();
            pq.pop();

            ans = (ans + cur) % MOD;

            cur--;

            if (cur > 0)
                pq.push(cur);
        }

        return (int)ans;
    }
};



class Solution {
  public:
    
    int n;
    int m;
    int ans;
    int row[4] = {0,0,-1,1};
    int col[4] = {-1,1,0,0};
    
    bool check(int i,int j){
        return i>=0 && j>=0 && i<n && j<m;
    }
    
    void find(int i,int j,int &d1,int &d2,vector<vector<int>>& mat,vector<vector<int>>& path,int &count){
        
        if(i==d1 && j==d2){
            ans =  max(ans,count);
            return;
        }
        
        
        path[i][j] = 1;
        
        for(int k=0;k<4;k++){
            
            
            int ni = i+row[k];
            int nj = j+col[k];
            
            if(check(ni,nj) && mat[ni][nj] && !path[ni][nj]){
                count++;
                find(ni,nj,d1,d2,mat,path,count);
                count--;
            }
            
        }
        
        path[i][j]=0;
        
    }
    
    int longestPath(vector<vector<int>>& mat, int xs, int ys, int xd, int yd) {
        // code here
        n = mat.size();
        m = mat[0].size();
        ans = -1;
        vector<vector<int>>path(n,vector<int>(m,0));
        int count = 0;
        find(xs,ys,xd,yd,mat,path,count);
        
        return ans;
    }
};

class Solution {
public:
    int countCompleteComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> A(n);

        for (auto& e : edges) {
            int u = e[0], v = e[1];
            A[u].push_back(v);
            A[v].push_back(u);
        }

        bitset<51> vis;
        int res = 0;

        for (int i = 0; i < n; i++) {
            bool state = vis.test(i);

            if (!state) {
                int V = 0, D = 0;

                auto dfs = [&](auto& self, int x) -> void {
                    V++;
                    D += A[x].size();
                    vis.set(x);

                    for (auto& state : A[x])
                        if (!vis.test(state))
                            self(self, state);
                };

                dfs(dfs, i);

                res += D == V * (V - 1);
            }
        }

        return res;
    }
};


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        A = defaultdict(list)
        for u, v in edges:
            A[u].append(v)
            A[v].append(u)

        vis, res = [False] * n, 0
        for i, state in enumerate(vis):
            if not state:
                D = V = 0

                def dfs(x):
                    nonlocal V, D
                    V += 1
                    D += len(A[x])
                    vis[x] = True

                    for state in A[x]:
                        if not vis[state]:
                            dfs(state)

                dfs(i)
                res += D == V * (V - 1)

        return res

class Solution {
public:
    vector<int> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        vector<pair<int, int>> newNums(n);
        for (int i = 0; i < n; i++)
            newNums[i] = {nums[i], i};
        sort(newNums.begin(), newNums.end());

        vector<int> getI(n);
        for (int i = 0; i < n; i++)
            getI[newNums[i].second] = i;

        vector<vector<int>> st(n, vector<int>(18));

        int r = 0;
        for (int i = 0; i < n; i++) {
            if (r < i) r = i;
            while (r + 1 < n &&
                   newNums[r + 1].first - newNums[r].first <= maxDiff &&
                   newNums[r + 1].first - newNums[i].first <= maxDiff)
                r++;
            st[i][0] = r;
        }

        for (int j = 1; j < 18; j++)
            for (int i = 0; i < n; i++)
                st[i][j] = st[st[i][j - 1]][j - 1];

        vector<int> ans(queries.size(), -1);
        for (int i = 0; i < (int)queries.size(); i++) {
            int a = getI[queries[i][0]];
            int b = getI[queries[i][1]];
            if (a > b) swap(a, b);
            if (a == b) { ans[i] = 0; continue; }

            int curr = a, steps = 0;
            for (int j = 17; j >= 0; j--)
                if (st[curr][j] < b) { curr = st[curr][j]; steps += (1 << j); }

            ans[i] = (st[curr][0] >= b) ? steps + 1 : -1;
        }
        return ans;
    }
};



class Solution {
    public int[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        int[][] newNums = new int[n][2];
        for (int i = 0; i < n; i++) newNums[i] = new int[]{nums[i], i};
        Arrays.sort(newNums, (a, b) -> a[0] - b[0]);

        int[] getI = new int[n];
        for (int i = 0; i < n; i++) getI[newNums[i][1]] = i;

        int[][] st = new int[n][18];
        int r = 0;
        for (int i = 0; i < n; i++) {
            if (r < i) r = i;
            while (r + 1 < n &&
                   newNums[r + 1][0] - newNums[r][0] <= maxDiff &&
                   newNums[r + 1][0] - newNums[i][0] <= maxDiff)
                r++;
            st[i][0] = r;
        }

        for (int j = 1; j < 18; j++)
            for (int i = 0; i < n; i++)
                st[i][j] = st[st[i][j - 1]][j - 1];

        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int a = getI[queries[i][0]], b = getI[queries[i][1]];
            if (a > b) { int t = a; a = b; b = t; }
            if (a == b) { ans[i] = 0; continue; }

            int curr = a, steps = 0;
            for (int j = 17; j >= 0; j--)
                if (st[curr][j] < b) { curr = st[curr][j]; steps += (1 << j); }

            ans[i] = (st[curr][0] >= b) ? steps + 1 : -1;
        }
        return ans;
    }
}



class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        new_nums = sorted(enumerate(nums), key=lambda x: x[1])
        get_i = [0] * n
        for i, (orig, _) in enumerate(new_nums):
            get_i[orig] = i

        LOG = 18
        st = [[0] * LOG for _ in range(n)]

        r = 0
        for i in range(n):
            if r < i: r = i
            while (r + 1 < n and
                   new_nums[r + 1][1] - new_nums[r][1] <= maxDiff and
                   new_nums[r + 1][1] - new_nums[i][1] <= maxDiff):
                r += 1
            st[i][0] = r

        for j in range(1, LOG):
            for i in range(n):
                st[i][j] = st[st[i][j - 1]][j - 1]

        ans = []
        for u, v in queries:
            a, b = get_i[u], get_i[v]
            if a > b: a, b = b, a
            if a == b: ans.append(0); continue

            curr, steps = a, 0
            for j in range(LOG - 1, -1, -1):
                if st[curr][j] < b:
                    curr = st[curr][j]
                    steps += (1 << j)

            ans.append(steps + 1 if st[curr][0] >= b else -1)

        return ans
		

class Solution {
  public:
    int getCount(int n) {
      
      if(n<=2)return 0;
      int ans = 1;
      int start = 1;
      int end = 1;
      int count = 0;
      
      int a = n/2;
      a++;
      
      while(end<=a && start<=end){
          
          if(ans==n) count++;
          
          if(ans<=n){
              end++;
              ans+=end;
          }
          else{
              ans-=start;
              start++;
          }
          
      }
      
      return count;
      
    }
};


class Solution {
public:
    vector<bool> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        vector<int> comp(n);
        comp[0] = 0;

        for (int i = 1; i < n; i++) {
            if (nums[i] - nums[i - 1] <= maxDiff)
                comp[i] = comp[i - 1];
            else
                comp[i] = comp[i - 1] + 1;
        }

        vector<bool> ans;
        ans.reserve(queries.size());

        for (auto &q : queries)
            ans.push_back(comp[q[0]] == comp[q[1]]);

        return ans;
    }
};


class Solution {
    public boolean[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        int[] comp = new int[n];
        comp[0] = 0;

        for (int i = 1; i < n; i++) {
            if (nums[i] - nums[i - 1] <= maxDiff) {
                comp[i] = comp[i - 1];
            } else {
                comp[i] = comp[i - 1] + 1;
            }
        }

        boolean[] ans = new boolean[queries.length];

        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0];
            int v = queries[i][1];
            ans[i] = (comp[u] == comp[v]);
        }

        return ans;
    }
}



class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        comp = [0] * n

        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                comp[i] = comp[i - 1]
            else:
                comp[i] = comp[i - 1] + 1

        return [comp[u] == comp[v] for u, v in queries]



class Solution {
    public int countKdivPairs(int[] arr, int k) {
        int[] ans = new int[k];
        int count = 0;
        for(int i:arr){
            count+=ans[i%k];
            ans[(-i%k+k)%k]++;
        }
        return count;
    }
}


MOD, MAX = 1000000007, 100001
pow = [1] * MAX
for i in range(1, MAX):
    pow[i] = (pow[i - 1] * 10) % MOD

class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        n, res = len(s), []
        A, B, Len = [[0] * (n + 1) for _ in range(3)]

        for i in range(n):
            d = int(s[i])
            A[i + 1] = A[i] + d
            B[i + 1] = (B[i] * 10 + d) % MOD if d else B[i]
            Len[i + 1] = Len[i] + (d > 0)

        res = []

        for l, r in queries:
            r += 1

            sub = (B[l] * pow[Len[r] - Len[l]]) % MOD
            x = (B[r] - sub) % MOD

            res.append((x * (A[r] - A[l])) % MOD)

        return res



class Solution {
  public:
    int countCoordinates(vector<vector<int>>& mat) {
        int n = mat.size();
        int m = mat[0].size();

        vector<vector<bool>> reachP(n, vector<bool>(m, false));
        vector<vector<bool>> reachQ(n, vector<bool>(m, false));

        int dr[4] = {1, -1, 0, 0};
        int dc[4] = {0, 0, 1, -1};

        auto dfs = [&](vector<pair<int, int>>& sources,
                       vector<vector<bool>>& visited) {
            vector<pair<int, int>> st;

            for (auto [r, c] : sources) {
                if (!visited[r][c]) {
                    visited[r][c] = true;
                    st.push_back({r, c});
                }
            }

            while (!st.empty()) {
                auto [r, c] = st.back();
                st.pop_back();

                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    if (nr < 0 || nr >= n || nc < 0 || nc >= m)
                        continue;

                    if (visited[nr][nc])
                        continue;

                    if (mat[nr][nc] < mat[r][c])
                        continue;

                    visited[nr][nc] = true;
                    st.push_back({nr, nc});
                }
            }
        };

        vector<pair<int, int>> sourcesP;
        for (int j = 0; j < m; j++)
            sourcesP.push_back({0, j});
        for (int i = 0; i < n; i++)
            sourcesP.push_back({i, 0});

        vector<pair<int, int>> sourcesQ;
        for (int j = 0; j < m; j++)
            sourcesQ.push_back({n - 1, j});
        for (int i = 0; i < n; i++)
            sourcesQ.push_back({i, m - 1});

        dfs(sourcesP, reachP);
        dfs(sourcesQ, reachQ);

        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (reachP[i][j] && reachQ[i][j])
                    answer++;
            }
        }

        return answer;
    }
};

class Solution {
  public:
    int row[4]={0,0,-1,1};
    int col[4]={-1,1,0,0};
    int n,m;
    void bfs(vector<vector<int>>& mat,queue<pair<int,int>>q,vector<vector<bool>>&visited){
        while(!q.empty()){
            int r=q.front().first;
            int c=q.front().second;
            q.pop();
            for(int k=0;k<4;k++){
                int nr=r+row[k];
                int nc=c+col[k];
                
                if(nr>=0 && nr<n && nc>=0 && nc<m && !visited[nr][nc] && mat[nr][nc]>=mat[r][c]){
                    visited[nr][nc]=1;
                    q.push({nr,nc});
                }
            }
        }
    }
    int countCoordinates(vector<vector<int>>& mat) {
        // code here
        n=mat.size();
        m=mat[0].size();
        queue<pair<int,int>>p,q;
        vector<vector<bool>>pvis(n,vector<bool>(m,0));
        vector<vector<bool>>qvis(n,vector<bool>(m,0));
        for(int i=0;i<n;i++){
            p.push({i,0});
            pvis[i][0]=1;
        }
        for(int j=0;j<m;j++){
            p.push({0,j});
            pvis[0][j]=1;
        }
        for(int i=0;i<n;i++){
            q.push({i,m-1});
            qvis[i][m-1]=1;
        }
        for(int j=0;j<m;j++){
            q.push({n-1,j});
            qvis[n-1][j]=1;
        }
        bfs(mat,p,pvis);
        bfs(mat,q,qvis);
        
        int cnt=0;
        
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(pvis[i][j] && qvis[i][j]){
                    cnt++;
                }
            }
        }
        return cnt;
    }
};

class Solution {
  public:
    int countCoordinates(vector<vector<int>>& mat) {
        int n = mat.size();
        int m = mat[0].size();

        vector<vector<bool>> reachP(n, vector<bool>(m, false));
        vector<vector<bool>> reachQ(n, vector<bool>(m, false));

        int dr[4] = {1, -1, 0, 0};
        int dc[4] = {0, 0, 1, -1};

        auto dfs = [&](vector<pair<int, int>>& sources,
                       vector<vector<bool>>& visited) {
            vector<pair<int, int>> st;

            for (auto [r, c] : sources) {
                if (!visited[r][c]) {
                    visited[r][c] = true;
                    st.push_back({r, c});
                }
            }

            while (!st.empty()) {
                auto [r, c] = st.back();
                st.pop_back();

                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    if (nr < 0 || nr >= n || nc < 0 || nc >= m)
                        continue;

                    if (visited[nr][nc])
                        continue;

                    if (mat[nr][nc] < mat[r][c])
                        continue;

                    visited[nr][nc] = true;
                    st.push_back({nr, nc});
                }
            }
        };

        vector<pair<int, int>> sourcesP;
        for (int j = 0; j < m; j++)
            sourcesP.push_back({0, j});
        for (int i = 0; i < n; i++)
            sourcesP.push_back({i, 0});

        vector<pair<int, int>> sourcesQ;
        for (int j = 0; j < m; j++)
            sourcesQ.push_back({n - 1, j});
        for (int i = 0; i < n; i++)
            sourcesQ.push_back({i, m - 1});

        dfs(sourcesP, reachP);
        dfs(sourcesQ, reachQ);

        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (reachP[i][j] && reachQ[i][j])
                    answer++;
            }
        }

        return answer;
    }
};


class Solution {
public:
    long long sumAndMultiply(int n) {
        long long x = 0, s = 0;
        for (char c : to_string(n))
            if (c != '0')
                x = x * 10 + c - '0', s += c - '0';
        return x * s;
    }
};




class Solution {
    public long sumAndMultiply(int n) {
        long x = 0, s = 0;
        for (char c : String.valueOf(n).toCharArray())
            if (c != '0') {
                x = x * 10 + c - '0';
                s += c - '0';
            }
        return x * s;
    }
}



class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [int(c) for c in str(n) if c != '0']
        x = int(''.join(map(str, digits))) if digits else 0
        return x * sum(digits)




const removeCoveredIntervals = A => {
    A.sort(([u, v], [x, y]) => (u - x) || (y - v));
    let res = 0, lo = 0;

    for (const [_, b] of A) {
        res += (b > lo);
        lo = Math.max(lo, b);
    }

    return res;
};


class Solution:
    def removeCoveredIntervals(self, A: List[List[int]]) -> int:
        A.sort(key=lambda x: (x[0], -x[1]))
        res = r = 0

        for st, end in A:
            res += end > r
            r = max(r, end)

        return res


class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& A) {
        ranges::sort(A, {}, [](auto& x) {
            return pair{x[0], -x[1]};
        });

        int res = 0, r = 0;

        for (auto& x : A) {
            res += x[1] > r;
            r = max(r, x[1]);
        }

        return res;
    }
};


class Solution {
  public:
    int maxPathSum(vector<int> &a, vector<int> &b) {
        // Code here
        int n = a.size();
        int m = b.size();
        int first = 0;
        int second = 0;
        int suma = a[0];
        int sumb = b[0];
        int ans = 0;
        
        while(first<n && second<m){
            
            if(a[first]==b[second]){ 
                ans+= max(suma,sumb);
                suma=0;
                sumb=0;
                first++;
                second++;
                
                if(first<n)
                suma+=a[first];
                if(second<m)
                sumb+=b[second];
            }
            else if(a[first]<b[second]){
                first++;
                if(first<n)
                suma+=a[first];
            }
            else{
                second++;
                if(second<m)
                sumb+=b[second];
            }
            
                
        }
        
        
        while(first<n){
            first++;
            if(first<n)
            suma+=a[first];
        }
        while(second<m){
            second++;
            if(second<m)
            sumb+=b[second];
        }
        
        ans+= max(suma,sumb);
        
        return ans;
    }
};


func pathsWithMaxScore(board []string) []int {
    const MOD int = 1000000007
    n := len(board)

    nextScore := make([]int, n+1)
    nextWays := make([]int, n+1)

    for j := 0; j <= n; j++ {
        nextScore[j] = -1
    }

    for i := n - 1; i >= 0; i-- {
        currScore := make([]int, n+1)
        currWays := make([]int, n+1)

        for j := 0; j <= n; j++ {
            currScore[j] = -1
        }

        for j := n - 1; j >= 0; j-- {
            cell := board[i][j]

            if cell == 'X' {
                continue
            }

            if cell == 'S' {
                currScore[j] = 0
                currWays[j] = 1
                continue
            }

            best := nextScore[j]
            if currScore[j+1] > best {
                best = currScore[j+1]
            }
            if nextScore[j+1] > best {
                best = nextScore[j+1]
            }

            if best == -1 {
                continue
            }

            ways := 0

            if nextScore[j] == best {
                ways = (ways + nextWays[j]) % MOD
            }
            if currScore[j+1] == best {
                ways = (ways + currWays[j+1]) % MOD
            }
            if nextScore[j+1] == best {
                ways = (ways + nextWays[j+1]) % MOD
            }

            value := 0
            if cell != 'E' {
                value = int(cell - '0')
            }

            currScore[j] = best + value
            currWays[j] = ways
        }

        nextScore = currScore
        nextWays = currWays
    }

    if nextScore[0] == -1 {
        return []int{0, 0}
    }

    return []int{nextScore[0], nextWays[0]}
}



class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        next_score = [-1] * (n + 1)
        next_ways = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            # Fresh arrays store the current row.
            curr_score = [-1] * (n + 1)
            curr_ways = [0] * (n + 1)

            for j in range(n - 1, -1, -1):
                cell = board[i][j]

                if cell == 'X':
                    continue

                if cell == 'S':
                    curr_score[j] = 0
                    curr_ways[j] = 1
                    continue

                best = max(
                    next_score[j],
                    curr_score[j + 1],
                    next_score[j + 1]
                )

                if best == -1:
                    continue

                ways = 0

                if next_score[j] == best:
                    ways += next_ways[j]
                if curr_score[j + 1] == best:
                    ways += curr_ways[j + 1]
                if next_score[j + 1] == best:
                    ways += next_ways[j + 1]

                value = 0 if cell == 'E' else int(cell)

                curr_score[j] = best + value
                curr_ways[j] = ways % MOD

            next_score = curr_score
            next_ways = curr_ways

        if next_score[0] == -1:
            return [0, 0]

        return [next_score[0], next_ways[0]]




// reduced space
constexpr int mod=1e9+7, N=100;
using ll=long long;
using int2=pair<int, int>;// (max sum, ways getting max sum)
constexpr int2 None={0, -1};
int2 dp[2][N];
class Solution {
public:
    static vector<int> pathsWithMaxScore(vector<string>& board) {
        const int n=board.size();
        bool last=(n-1)&1;
        fill_n(dp[last], n, None);// fill with {0, -1}
        dp[last][n-1]={0, 1};
        // last row
        for(int j=n-2; j>=0; j--){
            const char c=board[n-1][j];
            if (c=='X') break;
            dp[last][j].first=dp[last][j+1].first+c-'0';
            dp[last][j].second=1;
        }
        board[0][0]='0';
        for(int i=n-2; i>=0; i--){
            const char cR=board[i][n-1];
            bool cur=i&1, prv=(i+1)&1;
            if (cR=='X' || dp[prv][n-1].second==-1) 
                dp[cur][n-1]=None;
            else 
                dp[cur][n-1]={dp[prv][n-1].first+cR-'0', 1};
            for(int j=n-2; j>=0; j--){
                const int c=board[i][j];
                if (c=='X'){
                    dp[cur][j]=None;
                    continue;
                }
                auto& [r0, r1]=dp[cur][j+1];
                auto& [d0, d1]=dp[prv][j];
                auto& [s0, s1]=dp[prv][j+1];
                int prvM=-1;
                if (r1>0) prvM=max(prvM, r0);
                if (d1>0) prvM=max(prvM, d0);
                if (s1>0) prvM=max(prvM, s0);
                if (prvM==-1) {
                    dp[cur][j]=None; 
                    continue;
                }
                ll ways=0;
                ways+=(r1>0 && prvM==r0)?r1:0;
                ways+=(d1>0 && prvM==d0)?d1:0;
                ways+=(s1>0 && prvM==s0)?s1:0;
                dp[cur][j]={prvM+c-'0',  ways%mod};
            }
        }
        auto& [sum, ways]=dp[0][0];
        return (ways<=0)?vector<int>({0, 0}):vector<int>({sum, ways});
    }
};
auto init = []() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();


class Solution {
    public int maxCharGap(String s) {
        int n = s.length();
        
        int[] index = new int[26];
        Arrays.fill(index, -1);
        
        int res = -1;
        for (int i=0; i<n; i++) {
            char ch = s.charAt(i);
            
            if (index[ch - 'a'] == -1) {
                index[ch - 'a'] = i;
            }
            else {
                res = Math.max(res, i - index[ch - 'a'] -1);
            }
        }
        return res;
    }
};

class Solution:
     def maxCharGap(self, s):
          # code here
          st = {}
          n = len(s)
          max_gap = -1
          for i in range(n):
               if s[i] in st:
                    gap = i - st[s[i]] - 1
                    max_gap = max(max_gap, gap)
               else:
                    st[s[i]] = i
          return max_gap




const minScore = (n, roads) => {
    const root = [...Array(n + 1).keys()];
    const find = i => root[i] === i ? i : root[i] = find(root[i]);


    for (const [x, y, _] of roads)
        root[find(x)] = find(y);

    roads = roads.filter(r => find(r[0]) === find(1));

    let min = Infinity;

    for (const [, , d] of roads)
        min = Math.min(min, d);

    return min;
};


class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        root = list(range(n + 1))

        def find(i: int) -> int:
            root[i] = find(root[i]) if root[i] != i else i
            return root[i]

        for x, y, _ in roads:
            root[find(x)] = find(y)

        res, g1 = 10001, find(1)
        for x, _, d in roads:
            if find(x) == g1:
                res = min(res, d)

        return res


class Solution {
public:
    int minScore(int n, vector<vector<int>>& roads) {
        vector<int> root(n + 1);
        iota(root.begin(), root.end(), 0);

        auto find = [&](this auto& self, int i) -> int {
            return root[i] == i ? i : root[i] = self(root[i]);
        };

        for (auto& r : roads)
            root[find(r[0])] = find(r[1]);

        int res = 10001;
        for (auto& r : roads)
            if (find(r[0]) == find(1))
                res = min(res, r[2]);

        return res;
    }
};

class Solution {
  public:
    int countSubstring(string& s) {
        // Code Here
        int count = 0;
        // unordered_map<int,int>mp1 , mp2;
        vector<int>mp1(s.size()*2+5 , 0) , mp2(s.size() *2 + 5);
        int ans = 0;
        int m = s.size();
        mp1[m] = 1;
        mp2[m] = 1;
        for(auto i: s){
            if(i == '1')count++;
            else count--;
            mp1[count +m ]++;
            mp2[count +m] = mp1[count + m] + mp2[m +count-1];
            ans+= mp2[m + count-1];
        }
        return ans;
    }
};


func findMaxPathScore(edges [][]int, online []bool, k int64) int {
	n := len(online)

	type Edge struct {
		to int
		w  int
	}

	graph := make([][]Edge, n)
	indegree := make([]int, n)

	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		graph[u] = append(graph[u], Edge{v, w})
		indegree[v]++
	}

	queue := make([]int, 0)
	for i := 0; i < n; i++ {
		if indegree[i] == 0 {
			queue = append(queue, i)
		}
	}

	topo := make([]int, 0)

	for head := 0; head < len(queue); head++ {
		u := queue[head]
		topo = append(topo, u)

		for _, e := range graph[u] {
			indegree[e.to]--
			if indegree[e.to] == 0 {
				queue = append(queue, e.to)
			}
		}
	}

	check := func(limit int) bool {
		const INF int64 = 1 << 60

		dp := make([]int64, n)
		for i := range dp {
			dp[i] = INF
		}
		dp[0] = 0

		for _, u := range topo {

			if dp[u] == INF {
				continue
			}

			if u != 0 && u != n-1 && !online[u] {
				continue
			}

			for _, e := range graph[u] {

				if e.w < limit {
					continue
				}

				if e.to != n-1 && !online[e.to] {
					continue
				}

				if dp[u]+int64(e.w) < dp[e.to] {
					dp[e.to] = dp[u] + int64(e.w)
				}
			}
		}

		return dp[n-1] <= k
	}

	left, right := 0, 1000000000
	ans := -1

	for left <= right {
		mid := left + (right-left)/2

		if check(mid) {
			ans = mid
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return ans
}


				
class Solution {
public:

    bool check(long long mid, vector<vector<pair<int, int>>> &adj, vector<int> &topo, vector<bool> &online, long long k, int n) {

        const long long INF = 1e18;
        vector<long long> dist(n, INF);
        dist[0] = 0;

        for (int u : topo) {
            if (dist[u] == INF) continue;

            // Intermediate offline nodes cannot be used
            if (u != 0 && u != n - 1 && !online[u]) continue;

            for (auto &[v, w] : adj[u]) {
                if (w < mid) continue;
                if (v != n - 1 && !online[v]) continue;

                dist[v] = min(dist[v], dist[u] + w);
            }
        }

        return dist[n - 1] <= k;
    }

    int findMaxPathScore(vector<vector<int>>& edges, vector<bool>& online, long long k) {
        int n = online.size();
        vector<vector<pair<int, int>>> adj(n);
        vector<int> indegree(n, 0);

        int mx = 0;

        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].push_back({v, w});
            indegree[v]++;
            mx = max(mx, w);
        }

        // Topological Sort
        queue<int> q;
        for (int i = 0; i < n; i++)
            if (indegree[i] == 0)
                q.push(i);

        vector<int> topo;

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            topo.push_back(u);

            for (auto &[v, w] : adj[u]) {
                if (--indegree[v] == 0)
                    q.push(v);
            }
        }

        long long low = 0, high = mx;
        int ans = -1;

        while (low <= high) {
            long long mid = (low + high) / 2;

            if (check(mid, adj, topo, online, k, n)) {
                ans = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return ans;
    }
};


class Solution {
    private boolean check(long mid, List<int[]>[] adj, List<Integer> topo,
                          boolean[] online, long k, int n) {

        long INF = (long) 1e18;
        long[] dist = new long[n];
        Arrays.fill(dist, INF);
        dist[0] = 0;

        for (int u : topo) {
            if (dist[u] == INF) continue;

            if (u != 0 && u != n - 1 && !online[u]) continue;

            for (int[] edge : adj[u]) {
                int v = edge[0];
                int w = edge[1];

                if (w < mid) continue;
                if (v != n - 1 && !online[v]) continue;

                dist[v] = Math.min(dist[v], dist[u] + w);
            }
        }

        return dist[n - 1] <= k;
    }

    public int findMaxPathScore(int[][] edges, boolean[] online, long k) {

        int n = online.length;

        List<int[]>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++)
            adj[i] = new ArrayList<>();

        int[] indegree = new int[n];

        int maxEdge = 0;

        for (int[] e : edges) {
            int u = e[0];
            int v = e[1];
            int w = e[2];

            adj[u].add(new int[]{v, w});
            indegree[v]++;
            maxEdge = Math.max(maxEdge, w);
        }

        Queue<Integer> q = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0)
                q.offer(i);
        }

        List<Integer> topo = new ArrayList<>();

        while (!q.isEmpty()) {
            int u = q.poll();
            topo.add(u);

            for (int[] edge : adj[u]) {
                int v = edge[0];
                indegree[v]--;

                if (indegree[v] == 0)
                    q.offer(v);
            }
        }

        long low = 0, high = maxEdge;
        int ans = -1;

        while (low <= high) {
            long mid = low + (high - low) / 2;

            if (check(mid, adj, topo, online, k, n)) {
                ans = (int) mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return ans;
    }
}




class Solution {
  public:
    int waysToIncreaseLCSBy1(string &s1, string &s2) {
        int n = s1.size(), m = s2.size();

        vector<vector<int>> pref(n + 1, vector<int>(m + 1, 0));

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (s1[i - 1] == s2[j - 1])
                    pref[i][j] = pref[i - 1][j - 1] + 1;
                else
                    pref[i][j] = max(pref[i - 1][j], pref[i][j - 1]);
            }
        }

        int lcs = pref[n][m];

        vector<vector<int>> suff(n + 1, vector<int>(m + 1, 0));

        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                if (s1[i] == s2[j])
                    suff[i][j] = suff[i + 1][j + 1] + 1;
                else
                    suff[i][j] = max(suff[i + 1][j], suff[i][j + 1]);
            }
        }

        int ans = 0;

        for (int pos = 0; pos <= n; pos++) {

            for (char ch = 'a'; ch <= 'z'; ch++) {

                bool ok = false;

                for (int j = 0; j < m && !ok; j++) {

                    if (s2[j] != ch)
                        continue;

                    if (pref[pos][j] + 1 + suff[pos][j + 1] == lcs + 1)
                        ok = true;
                }

                if (ok)
                    ans++;
            }
        }

        return ans;
    }
};


class Solution:
    def check(self, mid, adj, topo, online, k, n):

        dist = [inf] * n
        dist[0] = 0

        for u in topo:

            if dist[u] == inf:
                continue

            if u != 0 and u != n - 1 and not online[u]:
                continue

            for v, w in adj[u]:

                if w < mid:
                    continue

                if v != n - 1 and not online[v]:
                    continue

                dist[v] = min(dist[v], dist[u] + w)

        return dist[n - 1] <= k

    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        adj = [[] for _ in range(n)]
        indegree = [0] * n

        max_edge = 0

        for u, v, w in edges:
            adj[u].append((v, w))
            indegree[v] += 1
            max_edge = max(max_edge, w)

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            u = q.popleft()
            topo.append(u)

            for v, _ in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        low, high = 0, max_edge
        ans = -1

        while low <= high:

            mid = (low + high) // 2

            if self.check(mid, adj, topo, online, k, n):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans  
		

ft_preds = []
for _, row in test_df.iterrows():
    emb1 = finetuned_model.encode(row['resume_text'])
    emb2 = finetuned_model.encode(row['job_description'])
    sim  = cosine_similarity([emb1], [emb2])[0][0]
    ft_preds.append(float(sim))

ft_mae  = mean_absolute_error(test_df['match_score'], ft_preds)
ft_rmse = np.sqrt(mean_squared_error(test_df['match_score'], ft_preds))

print(f'\nFine-tuned Model — Test Set Performance')
print(f'  MAE:  {ft_mae:.4f}')
print(f'  RMSE: {ft_rmse:.4f}')


# Side-by-side comparison
print('=' * 50)
print('MODEL COMPARISON')
print('=' * 50)
print(f'  Base MAE:         {base_mae:.4f}')
print(f'  Fine-tuned MAE:   {ft_mae:.4f}')
print(f'  Improvement:      {(base_mae - ft_mae)/base_mae*100:.1f}%')
print('=' * 50)

# Scatter plots: base vs fine-tuned
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
colors = test_df['match_label'].map({'low':'red','medium':'orange','high':'green'})

for ax, preds, title, mae in [
    (axes[0], base_preds, 'Base Model', base_mae),
    (axes[1], ft_preds,   'Fine-tuned Model', ft_mae),
]:
    ax.scatter(test_df['match_score'], preds, c=colors, alpha=0.7)
    ax.plot([0,1],[0,1],'k--', label='Perfect')
    ax.set_xlabel('Ground Truth match_score')
    ax.set_ylabel('Predicted Similarity')
    ax.set_title(f'{title} (MAE: {mae:.4f})', fontweight='bold')
    ax.grid(True, alpha=0.3)

from matplotlib.patches import Patch
fig.legend(handles=[
    Patch(color='green', label='high'),
    Patch(color='orange', label='medium'),
    Patch(color='red', label='low'),
], loc='lower center', ncol=3)
plt.tight_layout()
plt.show()

metadata = {
    'base_model':       'all-mpnet-base-v2',
    'dataset':          'merged_dataset_clean.csv',
    'total_pairs':      len(df),
    'train_pairs':      len(train_df),
    'val_pairs':        len(val_df),
    'test_pairs':       len(test_df),
    'epochs':           10,
    'batch_size':       16,
    'base_mae':         round(float(base_mae), 4),
    'finetuned_mae':    round(float(ft_mae), 4),
    'improvement_pct':  round((base_mae - ft_mae) / base_mae * 100, 2),
}

with open('models/finetuned-bert/metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)

print('Saved: models/finetuned-bert/')
print(json.dumps(metadata, indent=2))

#Production Pipeline Test

def score_resume_against_jd(resume_text, jd_text, model):
 
    emb_resume = model.encode(resume_text, convert_to_numpy=True)
    emb_jd     = model.encode(jd_text,     convert_to_numpy=True)
    score      = cosine_similarity([emb_resume], [emb_jd])[0][0]
    return float(score)


# Test with realistic cases
test_cases = [
    {
        'label':  'HIGH match expected',
        'resume': 'Senior Python developer with 6 years experience. Built REST APIs using FastAPI and Django. Proficient in PostgreSQL, Docker, and AWS deployment.',
        'jd':     'We need a Python backend engineer with FastAPI or Django experience. Must know SQL databases and cloud deployment.',
    },
    {
        'label':  'MEDIUM match expected',
        'resume': 'Frontend developer with 3 years React and TypeScript experience. Some Node.js and Express for small APIs.',
        'jd':     'Full stack engineer needed. React frontend required, strong Python backend preferred. 4+ years experience.',
    },
    {
        'label':  'LOW match expected',
        'resume': 'Executive Chef with 12 years experience in fine dining. Expert in French cuisine, menu planning, and kitchen management.',
        'jd':     'Data Scientist with Python, machine learning, and SQL experience required.',
    },
]

print('Production Pipeline Test')
print('=' * 60)
for case in test_cases:
    score = score_resume_against_jd(case['resume'], case['jd'], finetuned_model)
    label = 'HIGH' if score > 0.70 else 'MEDIUM' if score > 0.45 else 'LOW'
    print(f"\n{case['label']}")
    print(f"  Predicted score: {score:.4f}  →  {label}")

class Solution {
    public int numberOfSubstrings(String s) {
        int res = 0;
        int[] p = {-1, -1, -1};

        for (int i = 0; i < s.length(); i++) {
            p[(s.charAt(i) & 31) - 1] = i;
            res += Math.min(p[0], Math.min(p[1], p[2])) + 1;
        }

        return res;
    }
}




class Solution {
public:
    int numberOfSubstrings(string s) {
        int res = 0;
        int p[3] = {-1, -1, -1};

        for (int i = 0; i < s.length(); i++) {
            p[(s[i] & 31) - 1] = i;
            res += min({p[0], p[1], p[2]}) + 1;
        }

        return res;
    }
};




const numberOfSubstrings = s => {
    let res = 0, p = [5e4, -1, -1, -1];

    for (let i = 0; i < s.length; i++) {
        p[s.charCodeAt(i) & 31] = i;
        res += Math.min(...p) + 1;
    }

    return res;
};



class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res, p = 0, [5e4, -1, -1, -1]

        for i, ch in enumerate(s):
            p[ord(ch) & 31] = i
            res += min(p) + 1

        return res



class Solution {
    public int numOfStrings(String[] patterns, String word) {
        int count = 0;
        for (String s : patterns)
            if (word.indexOf(s) != -1) count++; // -1 when not found
        return count;
    }
}

class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        int count = 0;
        for (const string& s : patterns)
            if (word.find(s) != string::npos) count++;
        return count;
    }
};


class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count = 0
        for s in patterns:
            if word.find(s) != -1: # return -1 when not found
                count += 1
        return count

class Solution {
  public:
  
    int mod=1e9+7;
    
    long long solve(int i, int prev, int adj, int n, int k, vector<vector<vector<int>>>&dp){
        
        if(i==n){
            if(adj==k) return 1;
            return 0;
        }
        
        if(prev!=-1 && dp[i][prev][adj]!=-1) return dp[i][prev][adj];
        
        long long one=0, zero=0;
        
        if(prev==1){
            one=solve(i+1, 1, adj+1, n, k, dp);
        }else{
            one=solve(i+1, 1, adj, n, k, dp);
        }
        zero=solve(i+1, 0, adj, n, k, dp);
        
        long long ans=(one+zero)%mod;
        
        if(prev!=-1) dp[i][prev][adj]=ans;
        
        return ans;
        
    }
  
    int countStrings(int n, int k) {
        // code here
        vector<vector<vector<int>>>dp(n, vector<vector<int>>(2, vector<int>(n, -1)));
        return solve(0, -1, 0, n, k, dp);
    }
};
class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int>& A) {
        sort(A.begin(), A.end());
        int n = A.size();

        A.front() = 1;
        for (int i = 1; i < n; i++)
            A[i] = min(A[i], A[i - 1] + 1);
        
        return A.back();
    }
};
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, A: list[int]) -> int:
        A.sort()
        n = len(A)

        A[0] = 1
        for i in range(1, n):
            A[i] = min(A[i], A[i - 1] + 1)
            
        return A[-1]


var countMajoritySubarrays = function(nums, target) {
    const n = nums.length;
    let pref = n;

    const freq = new Array(2 * n + 1).fill(0);
    freq[n] = 1;

    let less = 0;
    let ans = 0;

    for (const num of nums) {
        if (num === target) {
            less += freq[pref];
            pref++;
        } else {
            pref--;
            less -= freq[pref];
        }

        freq[pref]++;
        ans += less;
    }

    return ans;
};


class Solution {
public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        int size = nums.size(), pref = size;

        vector<int> freq(2 * size + 1);
        freq[size] = 1;

        long long less = 0, ans = 0;

        for (int num : nums) {
            if (num == target)
                less += freq[pref++];
            else
                less -= freq[--pref];

            ++freq[pref];
            ans += less;
        }

        return ans;
    }
};



class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pref = n

        freq = [0] * (2 * n + 1)
        freq[n] = 1

        less = 0
        ans = 0

        for num in nums:
            if num == target:
                less += freq[pref]
                pref += 1
            else:
                pref -= 1
                less -= freq[pref]

            freq[pref] += 1
            ans += less

        return ans





class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        cnt = 0

        for i in range(n):
            freq = 0

            for j in range(i, n):
                if nums[j] == target:
                    freq += 1

                length = j - i + 1

                if freq > length // 2:
                    cnt += 1

        return cnt

func countMajoritySubarrays(nums []int, target int) int64 {
    n := len(nums)
    var ans int64 = 0

    for l := 0; l < n; l++ {
        targetCount := 0

        for r := l; r < n; r++ {
            if nums[r] == target {
                targetCount++
            }

            length := r - l + 1

            if targetCount > length/2 {
                ans++
            }
        }
    }

    return ans
}



class Solution {
public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size();
        long long ans = 0;

        for (int l = 0; l < n; l++) {
            int targetCount = 0;

            for (int r = l; r < n; r++) {
                if (nums[r] == target) {
                    targetCount++;
                }

                int len = r - l + 1;

                if (targetCount > len / 2) {
                    ans++;
                }
            }
        }

        return ans;
    }
};class Solution {
public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size();
        long long ans = 0;

        for (int l = 0; l < n; l++) {
            int targetCount = 0;

            for (int r = l; r < n; r++) {
                if (nums[r] == target) {
                    targetCount++;
                }

                int len = r - l + 1;

                if (targetCount > len / 2) {
                    ans++;
                }
            }
        }

        return ans;
    }
};

var countMajoritySubarrays = function(nums, target) {
    const n = nums.length;
    let ans = 0;

    for (let l = 0; l < n; l++) {
        let targetCount = 0;

        for (let r = l; r < n; r++) {
            if (nums[r] === target) {
                targetCount++;
            }

            const len = r - l + 1;

            if (targetCount > Math.floor(len / 2)) {
                ans++;
            }
        }
    }

    return ans;
};


class Solution {
    public int countMajoritySubarrays(int[] nums, int target) {
        int n = nums.length;
        int ans = 0;

        for (int l = 0; l < n; l++) {
            int targetCount = 0;

            for (int r = l; r < n; r++) {
                if (nums[r] == target) {
                    targetCount++;
                }

                int len = r - l + 1;

                if (targetCount > len / 2) {
                    ans++;
                }
            }
        }

        return ans;
    }
}


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0

        for l in range(n):
            target_count = 0

            for r in range(l, n):
                if nums[r] == target:
                    target_count += 1

                length = r - l + 1

                if target_count > length // 2:
                    ans += 1

        return ans


func zigZagArrays(n int, l int, r int) int {
	const MOD int64 = 1000000007

	m := r - l + 1
	sz := 2 * m

	multiply := func(A, B [][]int64) [][]int64 {
		C := make([][]int64, sz)

		for i := 0; i < sz; i++ {
			C[i] = make([]int64, sz)

			for k := 0; k < sz; k++ {
				if A[i][k] == 0 {
					continue
				}

				cur := A[i][k]

				for j := 0; j < sz; j++ {
					if B[k][j] == 0 {
						continue
					}

					C[i][j] = (C[i][j] + cur*B[k][j]) % MOD
				}
			}
		}

		return C
	}

	T := make([][]int64, sz)

	for i := 0; i < sz; i++ {
		T[i] = make([]int64, sz)
	}

	for x := 0; x < m; x++ {

		for y := x + 1; y < m; y++ {
			T[x][m+y] = 1
		}

		for y := 0; y < x; y++ {
			T[m+x][y] = 1
		}
	}

	result := make([][]int64, sz)

	for i := 0; i < sz; i++ {
		result[i] = make([]int64, sz)
		result[i][i] = 1
	}

	power := n - 1

	for power > 0 {
		if power&1 == 1 {
			result = multiply(result, T)
		}

		T = multiply(T, T)
		power >>= 1
	}

	var answer int64 = 0

	for i := 0; i < sz; i++ {
		var rowSum int64 = 0

		for j := 0; j < sz; j++ {
			rowSum = (rowSum + result[i][j]) % MOD
		}

		answer = (answer + rowSum) % MOD
	}

	return int(answer)
}


/**
 * @param {number} n
 * @param {number} l
 * @param {number} r
 * @return {number}
 */
var zigZagArrays = function(n, l, r) {
    const MOD = 1000000007n;

    const m = r - l + 1;
    const sz = 2 * m;

    const multiply = (A, B) => {
        const C = Array.from(
            { length: sz },
            () => Array(sz).fill(0n)
        );

        for (let i = 0; i < sz; i++) {
            for (let k = 0; k < sz; k++) {
                if (A[i][k] === 0n) continue;

                const cur = A[i][k];

                for (let j = 0; j < sz; j++) {
                    if (B[k][j] === 0n) continue;

                    C[i][j] = (C[i][j] + cur * B[k][j]) % MOD;
                }
            }
        }

        return C;
    };

    let T = Array.from(
        { length: sz },
        () => Array(sz).fill(0n)
    );

    for (let x = 0; x < m; x++) {

        for (let y = x + 1; y < m; y++) {
            T[x][m + y] = 1n;
        }

        for (let y = 0; y < x; y++) {
            T[m + x][y] = 1n;
        }
    }

    let result = Array.from(
        { length: sz },
        (_, i) =>
            Array.from(
                { length: sz },
                (_, j) => (i === j ? 1n : 0n)
            )
    );

    let power = BigInt(n - 1);

    while (power > 0n) {
        if (power & 1n) {
            result = multiply(result, T);
        }

        T = multiply(T, T);
        power >>= 1n;
    }

    let answer = 0n;

    for (let i = 0; i < sz; i++) {
        let rowSum = 0n;

        for (let j = 0; j < sz; j++) {
            rowSum = (rowSum + result[i][j]) % MOD;
        }

        answer = (answer + rowSum) % MOD;
    }

    return Number(answer);
};


class Solution {
    private static final long MOD = 1_000_000_007L;

    private long[][] multiply(long[][] A, long[][] B) {
        int sz = A.length;

        long[][] C = new long[sz][sz];

        for (int i = 0; i < sz; i++) {
            for (int k = 0; k < sz; k++) {
                if (A[i][k] == 0) continue;

                long cur = A[i][k];

                for (int j = 0; j < sz; j++) {
                    if (B[k][j] == 0) continue;

                    C[i][j] = (C[i][j] + cur * B[k][j]) % MOD;
                }
            }
        }

        return C;
    }

    public int zigZagArrays(int n, int l, int r) {
        int m = r - l + 1;
        int sz = 2 * m;

        long[][] T = new long[sz][sz];

        for (int x = 0; x < m; x++) {

            for (int y = x + 1; y < m; y++) {
                T[x][m + y] = 1;
            }

            for (int y = 0; y < x; y++) {
                T[m + x][y] = 1;
            }
        }

        long[][] result = new long[sz][sz];
        for (int i = 0; i < sz; i++) {
            result[i][i] = 1;
        }

        long power = n - 1;

        while (power > 0) {
            if ((power & 1) == 1) {
                result = multiply(result, T);
            }

            T = multiply(T, T);
            power >>= 1;
        }

        long answer = 0;

        for (int i = 0; i < sz; i++) {
            long rowSum = 0;

            for (int j = 0; j < sz; j++) {
                rowSum = (rowSum + result[i][j]) % MOD;
            }

            answer = (answer + rowSum) % MOD;
        }

        return (int) answer;
    }
}


class Solution {
public:
    static const long long MOD = 1000000007LL;

    vector<vector<long long>> multiply(
        const vector<vector<long long>>& A,
        const vector<vector<long long>>& B
    ) {
        int sz = A.size();

        vector<vector<long long>> C(sz, vector<long long>(sz, 0));

        for (int i = 0; i < sz; i++) {
            for (int k = 0; k < sz; k++) {
                if (A[i][k] == 0) continue;

                long long cur = A[i][k];

                for (int j = 0; j < sz; j++) {
                    if (B[k][j] == 0) continue;

                    C[i][j] = (C[i][j] + cur * B[k][j]) % MOD;
                }
            }
        }

        return C;
    }

    int zigZagArrays(int n, int l, int r) {
        int m = r - l + 1;
        int sz = 2 * m;

        vector<vector<long long>> T(sz, vector<long long>(sz, 0));

        for (int x = 0; x < m; x++) {

            for (int y = x + 1; y < m; y++) {
                T[x][m + y] = 1;
            }

            for (int y = 0; y < x; y++) {
                T[m + x][y] = 1;
            }
        }

        vector<vector<long long>> result(sz, vector<long long>(sz, 0));
        for (int i = 0; i < sz; i++) {
            result[i][i] = 1;
        }

        long long power = n - 1;

        while (power > 0) {
            if (power & 1) {
                result = multiply(result, T);
            }

            T = multiply(T, T);
            power >>= 1;
        }

        vector<long long> initial(sz, 1);

        long long answer = 0;

        for (int i = 0; i < sz; i++) {
            long long rowSum = 0;

            for (int j = 0; j < sz; j++) {
                rowSum = (rowSum + result[i][j]) % MOD;
            }

            answer = (answer + rowSum) % MOD;
        }

        return (int)answer;
    }
};

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007

        m = r - l + 1
        sz = 2 * m

        def multiply(A, B):
            C = [[0] * sz for _ in range(sz)]

            for i in range(sz):
                for k in range(sz):
                    if A[i][k] == 0:
                        continue

                    cur = A[i][k]

                    for j in range(sz):
                        if B[k][j] == 0:
                            continue

                        C[i][j] = (C[i][j] + cur * B[k][j]) % MOD

            return C

        T = [[0] * sz for _ in range(sz)]

        for x in range(m):

            for y in range(x + 1, m):
                T[x][m + y] = 1

            for y in range(x):
                T[m + x][y] = 1

        result = [[0] * sz for _ in range(sz)]
        for i in range(sz):
            result[i][i] = 1

        power = n - 1

        while power:
            if power & 1:
                result = multiply(result, T)

            T = multiply(T, T)
            power >>= 1

        answer = 0

        for i in range(sz):
            row_sum = sum(result[i]) % MOD
            answer = (answer + row_sum) % MOD

        return answer

class Solution {
    private static final int MOD = 1000000007;

    public int zigZagArrays(int n, int l, int r) {
        int m = r - l + 1;
        int[] dp = new int[m];
        Arrays.fill(dp, 1);

        for (int i = 2; i <= n; i++) {
            int sum = 0;
            if ((i & 1) == 0)
                for (int j = 0; j < m; j++) {
                    int t = dp[j];
                    dp[j] = sum;
                    sum = (sum + t) % MOD;
                }
            else
                for (int j = m - 1; j >= 0; j--) {
                    int t = dp[j];
                    dp[j] = sum;
                    sum = (sum + t) % MOD;
                }
        }

        int res = 0;
        for (int j = 0; j < m; j++)
            res = (res + dp[j]) % MOD;

        return (res << 1) % MOD;
    }
}




class Solution {
public:
    static constexpr int MOD = 1000000007;
    int zigZagArrays(int n, int l, int r) {
        int m = r - l + 1;
        vector<int> dp(m, 1);

        for (int i = 2; i <= n; i++) {
            reverse(dp.begin(), dp.end());
            int sum = 0;
            for (auto& d : dp)
                sum = (sum + exchange(d, sum)) % MOD;
        }

        return ((accumulate(dp.begin(), dp.end(), 0LL) % MOD) << 1) % MOD;
    }
};


const mod = 1e9 + 7;

const zigZagArrays = (n, l, r) => {
    const m = r - l + 1;
    const dp = Array(m).fill(1);

    for (let i = 2; i <= n; i++) {
        dp.reverse();
        let sum = 0;
        for (let j = 0; j < m; j++)
            [dp[j], sum] = [sum, (sum + dp[j]) % mod];
    }

    return (dp.reduce((a, c) => (a + c) % mod, 0) << 1) % mod;
};


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007
        m = r - l + 1
        dp = [1] * m

        for i in range(2, n + 1):
            dp.reverse()
            s = 0
            for j in range(m):
                dp[j], s = s, (s + dp[j]) % MOD

        return (sum(dp) % MOD << 1) % MOD

class Solution:
    def maxArea(self, height):
        # code here
        i, j = 0, len(height) - 1
        maxi = -1
        while i < j:
            maxi = max(maxi, (j - i - 1) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
                
        return maxi
		

class Solution {
    public int maxNumberOfBalloons(String s) {
        int[] f = new int[5];
        String t = "balon";

        for (int i = 0; i < s.length(); i++)
            for (int j = 0; j < 5; j++)
                if (s.charAt(i) == t.charAt(j))
                    f[j]++;

        f[2] >>= 1;
        f[3] >>= 1;

        return Arrays.stream(f).min().getAsInt();
    }
}



const maxNumberOfBalloons = (t, f = _.countBy(t)) => Math.min(
    f.b | 0, f.a | 0, f.l >> 1, f.o >> 1, f.n | 0
);



class Solution {
public:
    int maxNumberOfBalloons(string t) {
        int f[5] = {0};
        string s = "balon";

        for (uint32_t ch : t)
            for (int i = 0; i < 5; i++)
                f[i] += !(ch ^ s[i]);

        return min({f[0], f[1], f[2] >> 1, f[3] >> 1, f[4]});
    }
};


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        f = Counter(text)
        return min(f["b"], f["a"], f["l"] >> 1, f["o"] >> 1, f["n"])
		


constexpr int M = 1e5 + 1;
int freq[M];
class Solution {
public:
    static int maxIceCream(vector<int>& costs, int coins) {
        int xMax = 0;
        for (int x : costs) {
            freq[x]++;
            xMax = max(xMax, x);
        }
        int cnt = 0;
        for (int x = 1; x <= xMax; x++) {
            const int f = freq[x];
            if (f == 0)
                continue;
            int buy = min(coins / x, f);
            if (buy == 0)
                break;
            cnt += buy;
            coins -= buy * x;
        }
        // reset for the next testcase
        for (int x : costs)
            freq[x] = 0;
        return cnt;
    }
};
auto init = []() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    return 'c';
}();


#pragma GCC optimize("O3, unroll
-loops")
static int freq[100001] = {0};
static int maxIceCream(int* costs, int n, int coins) {
    int xMax = 0;
    for (int i = 0; i < n; i++) {
        const int x = costs[i];
        freq[x]++;
        xMax += (-(x > xMax) & x - xMax);
    }
    int cnt = 0;
    for (int x = 1; x <= xMax && coins > 0; x++) {
        const int f = freq[x];
        if (f == 0)
            continue;
        int q = coins / x;
        int buy = fmin(q, f);
        cnt += buy;
        coins -= buy * x;
    }
    // reset
    for (int i = 0; i < n; i++)
        freq[costs[i]] = 0;
    return cnt;
}


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

		

class Solution {
    public int maxBuilding(int num, int[][] restrictions) {
        List<int[]> r = new ArrayList<>(Arrays.asList(restrictions));
        r.add(new int[]{1, 0});
        r.sort((a, b) -> Integer.compare(a[0], b[0]));
        int n = r.size();

        for (int i = 1; i < n; i++)
            r.get(i)[1] = yCap(r.get(i - 1), r.get(i));

        for (int i = n - 2; i >= 0; i--)
            r.get(i)[1] = yCap(r.get(i + 1), r.get(i));

        int res = 0;
        for (int i = 1; i < n; i++)
            res = Math.max(res, yPeak(r.get(i - 1), r.get(i)));

        return Math.max(res, r.get(n - 1)[1] + num - r.get(n - 1)[0]);
    }

    int yCap(int[] l, int[] b) {
        return Math.min(b[1], l[1] + Math.abs(b[0] - l[0]));
    }

    int yPeak(int[] l, int[] b) {
        return (l[1] + b[1] + b[0] - l[0]) >> 1;
    }
}


const { abs, max, min } = Math;

const maxBuilding = (num, r) => {
    r.push([1, 0]);
    r.sort(([a], [b]) => a - b);
    const n = r.length;

    for (let i = 1; i < n; i++)
        r[i][1] = yCap(r[i - 1], r[i]);

    for (let i = n - 2; i >= 0; i--)
        r[i][1] = yCap(r[i + 1], r[i]);

    let res = 0;
    for (let i = 1; i < n; i++)
        res = max(res, yPeak(r[i - 1], r[i]));

    return max(res, r[n - 1][1] + num - r[n - 1][0]);
};

const yCap = ([x1, y1], [x2, y2]) => min(y2, y1 + abs(x2 - x1));
const yPeak = ([x1, y1], [x2, y2]) => (y1 + y2 + x2 - x1) >> 1;

class Solution {
public:
    int maxBuilding(int num, vector<vector<int>>& r) {
        r.push_back({1, 0});
        sort(r.begin(), r.end());
        int n = r.size();

        for (int i = 1; i < n; i++)
            r[i][1] = yCap(r[i - 1], r[i]);

        for (int i = n - 2; i >= 0; i--)
            r[i][1] = yCap(r[i + 1], r[i]);

        int res = 0;
        for (int i = 1; i < n; i++)
            res = max(res, yPeak(r[i - 1], r[i]));

        return max(res, r[n - 1][1] + num - r[n - 1][0]);
    }

    int yCap(vector<int>& l, vector<int>& r) {
        int x1 = l[0], y1 = l[1], x2 = r[0], y2 = r[1];
        return min(y2, y1 + abs(x2 - x1));
    }

    int yPeak(vector<int>& l, vector<int>& r) {
        int x1 = l[0], y1 = l[1], x2 = r[0], y2 = r[1];
        return (y1 + y2 + x2 - x1) >> 1;
    }
};


class Solution:
    def maxBuilding(self, num: int, r: list[list[int]]) -> int:
        r.append([1, 0])
        r.sort()
        n = len(r)

        def yCap(x1, y1, x2, y2):
            return min(y2, y1 + abs(x2 - x1))

        def yPeak(x1, y1, x2, y2):
            return (y1 + y2 + x2 - x1) >> 1
        
        for i in range(1, n):
            r[i][1] = yCap(*r[i - 1], *r[i])

        for i in range(n - 2, -1, -1):
            r[i][1] = yCap(*r[i + 1], *r[i])

        res = 0
        for i in range(1, n):
            res = max(res, yPeak(*r[i - 1], *r[i]))

        return max(res, r[-1][1] + num - r[-1][0])


class Solution:
    def getLastDigit(self, a, b):
        # code here
        a = int(a)
        b = int(b)
        if b == 0:
            return 1
        a = a%10
        rem = b % 4
        vals = {
        0: {1:0, 2:0, 3:0, 0:0},
        1: {1:1, 2:1, 3:1, 0:1},
        2: {1:2, 2:4, 3:8, 0:6},
        3: {1:3, 2:9, 3:7, 0:1},
        4: {1:4, 2:6, 3:4, 0:6},
        5: {1:5, 2:5, 3:5, 0:5},
        6: {1:6, 2:6, 3:6, 0:6},
        7: {1:7, 2:9, 3:3, 0:1},
        8: {1:8, 2:4, 3:2, 0:6},
        9: {1:9, 2:1, 3:9, 0:1}}
        
        return vals[a][rem]


class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int ans = 0, sum = 0;

        for (auto& it : gain) {
            sum += it;
            int d = sum - ans;
            ans += d & ~(d >> 0x1F);
        }

        return ans;
    }
};




class Solution {
  public:
    vector<int> optimalArray(vector<int> &arr) {
        int n = arr.size();

        vector<long long> pref(n + 1, 0);

        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + arr[i];
        }

        vector<int> ans(n);

        for (int i = 0; i < n; i++) {

            int mid = i / 2;

            long long median = arr[mid];

            long long leftCost =
                median * (mid + 1LL) - pref[mid + 1];

            long long rightCost =
                (pref[i + 1] - pref[mid + 1]) -
                median * (i - mid);

            ans[i] = (int)(leftCost + rightCost);
        }

        return ans;
    }
};

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = acc = 0

        for it in gain:
            acc += it
            d = acc - ans
            ans += d & ~(d >> 0x1F)

        return ans


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = 6.0 * minutes
        hour_angle = 30.0 * (hour % 12) + 0.5 * minutes

        diff = abs(hour_angle - minute_angle)

        return min(diff, 360.0 - diff)

class Solution {
    public double angleClock(int hour, int minutes) {
        double x = hour + minutes / 60.0;
        double diff = (11.0 * x) % 12.0;
        return Math.min(diff, 12.0 - diff) * 30.0;
    }
}


const angleClock = (hour, minutes) => {
    const x = hour + minutes / 60;
    const diff = (11 * x) % 12;
    return Math.min(diff, 12 - diff) * 30;
};


class Solution {
public:
    double angleClock(int hour, int minutes) {
        double x = hour + minutes / 60.0;
        double diff = fmod(11.0 * x, 12.0);
        return min(diff, 12.0 - diff) * 30.0;
    }
};

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        x = hour + minutes / 60
        diff = (11 * x) % 12
        return min(diff, 12 - diff) * 30

func processStr(s string, k int64) byte {
    var len int64 = 0

    // Step 1
    for _, c := range s {
        if c == '*' {
            if len > 0 {
                len--
            }
        } else if c == '#' {
            len *= 2
        } else if c != '%' {
            len++
        }
    }

    if k >= len {
        return '.'
    }

    // Step 2
    for i := len(s) - 1; i >= 0; i-- {
        c := s[i]

        if c == '*' {
            len++
        } else if c == '#' {
            half := len / 2
            if k >= half {
                k -= half
            }
            len = half
        } else if c == '%' {
            k = len - 1 - k
        } else {
            if k == len-1 {
                return c
            }
            len--
        }
    }

    return '.'
}


const processStr = (s, k) => {
    const n = s.length;
    const lens = [];
    let len = 0;

    for (const c of s) {
        if (c === '*')
            len = Math.max(len - 1, 0);
        else if (c === '#')
            len *= 2;
        else if (c !== '%')
            len++;
        
        lens.push(len);
    }

    if (k >= len) return '.';

    for (let i = n - 1; ; i--) {
        switch (s[i]) {
            case '*':
                break;
            case '#':
                if (k >= Math.floor(lens[i] / 2))
                    k -= Math.floor(lens[i] / 2);
                break;
            case '%':
                k = lens[i] - 1 - k;
                break;
            default:
                if (lens[i] === k + 1)
                    return s[i];
        }
    }
};


class Solution {
    typedef long long ll;
public:
    char processStr(string s, ll k) {
        int n = s.size();
        vector<ll> lens;
        ll len = 0;

        for (auto& ch : s) {
            if (ch == '*')
                len = max(len - 1, 0LL);
            else if (ch == '#')
                len *= 2;
            else if (ch != '%')
                len++;

            lens.push_back(len);
        }

        if (k >= len) return '.';

        for (int i = n - 1;; i--) {
            switch (s[i]) {
            case '*':
                break;
            case '#':
                if (k >= lens[i] / 2)
                    k -= lens[i] / 2;
                break;
            case '%':
                k = lens[i] - 1 - k;
                break;
            default: // s[i] is a character
                if (lens[i] == k + 1)
                    return s[i];
            }
        }
    }
};


class Solution {
    public char processStr(String s, long k) {
        int n = s.length();
        long[] lens = new long[n];
        long len = 0;

        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == '*')
                len = Math.max(len - 1, 0L);
            else if (c == '#')
                len *= 2;
            else if (c != '%')
                len++;
            
            lens[i] = len;
        }

        if (k >= len) return '.';

        for (int i = n - 1; ; i--) {
            char c = s.charAt(i);
            switch (c) {
                case '*':
                    break;
                case '#':
                    if (k >= lens[i] / 2)
                        k -= lens[i] / 2;
                    break;
                case '%':
                    k = lens[i] - 1 - k;
                    break;
                default:
                    if (lens[i] == k + 1)
                        return c;
            }
        }
    }
}


class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lens = []
        ln = 0

        for c in s:
            if c == '*':
                ln = max(ln - 1, 0)
            elif c == '#':
                ln *= 2
            elif c != '%':
                ln += 1
            
            lens.append(ln)

        if k >= ln:
            return '.'

        for i in range(n - 1, -1, -1):
            c = s[i]
            if c == '*':
                continue
            elif c == '#':
                if k >= lens[i] // 2:
                    k -= lens[i] // 2
            elif c == '%':
                k = lens[i] - 1 - k
            else:
                if lens[i] == k + 1:
                    return c


//translated using AI
var processStr = function(s) {
    let res = [];
    let n = s.length;

    for (let i = 0; i < n; i++) {
        let ch = s[i];

        if (ch === '*') {
            if (res.length !== 0) {
                res.pop();
            }
        } 
        else if (ch === '#') {
            res.push(...res);
        } 
        else if (ch === '%') {
            res.reverse();
        } 
        else if (ch >= 'a' && ch <= 'z') {
            res.push(ch);
        }
    }

    return res.join('');
};



class Solution {
    public String processStr(String s) {
        StringBuilder sb = new StringBuilder();
        int n = s.length();

        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);

            if (ch == '*') {
                if (sb.length() != 0) {
                    sb.deleteCharAt(sb.length() - 1);
                }
            } 
            else if (ch == '#') {
                sb.append(sb);
            } 
            else if (ch == '%') {
                sb.reverse();
            } 
            else if (ch >= 'a' && ch <= 'z') {
                sb.append(ch);
            }
        }

        return sb.toString();
    }
}


//translated using AI
class Solution {
public:
    string processStr(string s) {
        string res;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            char ch = s[i];

            if (ch == '*') {
                if (res.length() != 0) {
                    res.pop_back();
                }
            } 
            else if (ch == '#') {
                res += res;
            } 
            else if (ch == '%') {
                reverse(res.begin(), res.end());
            } 
            else if (ch >= 'a' && ch <= 'z') {
                res.push_back(ch);
            }
        }

        return res;
    }
};


#translated using AI
class Solution:
    def processStr(self, s: str) -> str:
        res = []
        n = len(s)

        for i in range(n):
            ch = s[i]

            if ch == '*':
                if len(res) != 0:
                    res.pop()
            elif ch == '#':
                res.extend(res)
            elif ch == '%':
                res.reverse()
            elif 'a' <= ch <= 'z':
                res.append(ch)

        return ''.join(res)


class Solution {
    public ListNode deleteMiddle(ListNode head) {
        if (head.next == null) return null;

        ListNode slow = head;
        ListNode fast = slow.next.next;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        slow.next = slow.next.next;
        return head;
    }
}



const deleteMiddle = head => {
    if (!head.next) return null;

    let slow = head;
    let fast = slow.next.next;

    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    slow.next = slow.next.next;
    return head;
};



class Solution {
public:
    ListNode* deleteMiddle(ListNode* head) {
        if (!head->next) return nullptr;

        ListNode* slow = head;
        ListNode* fast = slow->next->next;

        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        slow->next = slow->next->next;
        return head;
    }
};



// Memory Deallocation
// LeetCode environment automatically frees the bypassed middle node


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return None

        slow = head
        fast = slow.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head
		


class Solution {
public:
    int pairSum(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* prev = nullptr;

        while (fast && fast->next) {
            fast = fast->next->next;
            swap(slow->next, prev);
            swap(prev, slow);
        }

        int res = 0;
        while (slow) {
            res = max(res, prev->val + slow->val);
            prev = prev->next;
            slow = slow->next;
        }

        return res;
    }
};

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev, slow = prev, slow, slow.next

        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev, slow = prev.next, slow.next

        return res

class Solution:
    dxn=[(0,1),(1,0),(0,-1),(-1,0)]
    def exitPoint(self, mat):
        n,m=len(mat),len(mat[0])
        ans=[0,0]
        p,i,j=0,0,0
        while 0<=i<n and 0<=j<m:
            if mat[i][j]==0:
                ans=[i,j]
                dx,dy=Solution.dxn[p]
                i+=dx
                j+=dy
            else:
                mat[i][j]=0
                p=(p+1)%4
        return ans


class Solution {
    public String mapWordWeights(String[] words, int[] weights) {
        StringBuilder ans = new StringBuilder();

        for (String word : words) {
            long sum = 0;

            for (char ch : word.toCharArray()) {
                sum += weights[ch - 'a'];
            }

            int remainder = (int)(sum % 26);
            ans.append((char)('z' - remainder));
        }

        return ans.toString();
    }
}


class Solution {
public:
    string mapWordWeights(vector<string>& words, vector<int>& weights) {
        string ans;

        for (string& word : words) {
            long long sum = 0;

            for (char ch : word) {
                sum += weights[ch - 'a'];
            }

            ans.push_back('z' - (sum % 26));
        }

        return ans;
    }
};



class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []

        for word in words:
            total = 0

            for ch in word:
                total += weights[ord(ch) - ord('a')]

            remainder = total % 26
            ans.append(chr(ord('z') - remainder))

        return "".join(ans)
		
func assignEdgeWeights(edges [][]int, queries [][]int) []int {
	const MOD = 1000000007

	n := len(edges) + 1

	LOG := 1
	for (1 << LOG) <= n {
		LOG++
	}

	graph := make([][]int, n+1)

	for _, e := range edges {
		u, v := e[0], e[1]

		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}

	depth := make([]int, n+1)

	up := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		up[i] = make([]int, LOG)
		for j := 0; j < LOG; j++ {
			up[i][j] = 1
		}
	}

	var dfs func(int, int)

	dfs = func(node, parent int) {
		up[node][0] = parent

		for j := 1; j < LOG; j++ {
			up[node][j] = up[up[node][j-1]][j-1]
		}

		for _, next := range graph[node] {
			if next == parent {
				continue
			}

			depth[next] = depth[node] + 1
			dfs(next, node)
		}
	}

	dfs(1, 1)

	lca := func(a, b int) int {
		if depth[a] < depth[b] {
			a, b = b, a
		}

		diff := depth[a] - depth[b]

		for j := LOG - 1; j >= 0; j-- {
			if ((diff >> j) & 1) == 1 {
				a = up[a][j]
			}
		}

		if a == b {
			return a
		}

		for j := LOG - 1; j >= 0; j-- {
			if up[a][j] != up[b][j] {
				a = up[a][j]
				b = up[b][j]
			}
		}

		return up[a][0]
	}

	pow2 := make([]int, n+1)
	pow2[0] = 1

	for i := 1; i <= n; i++ {
		pow2[i] = int((int64(pow2[i-1]) * 2) % MOD)
	}

	ans := make([]int, len(queries))

	for i, q := range queries {
		u, v := q[0], q[1]

		ancestor := lca(u, v)

		dist := depth[u] + depth[v] - 2*depth[ancestor]

		if dist == 0 {
			ans[i] = 0
		} else {
			ans[i] = pow2[dist-1]
		}
	}

	return ans
}

class Solution {
    static final int MOD = 1000000007;

    int LOG;
    int[] depth;
    int[][] up;
    java.util.List<Integer>[] graph;

    void dfs(int node, int parent) {
        up[node][0] = parent;

        for (int j = 1; j < LOG; j++) {
            up[node][j] = up[up[node][j - 1]][j - 1];
        }

        for (int next : graph[node]) {
            if (next == parent) continue;

            depth[next] = depth[node] + 1;
            dfs(next, node);
        }
    }

    int lca(int a, int b) {
        if (depth[a] < depth[b]) {
            int temp = a;
            a = b;
            b = temp;
        }

        int diff = depth[a] - depth[b];

        for (int j = LOG - 1; j >= 0; j--) {
            if (((diff >> j) & 1) == 1) {
                a = up[a][j];
            }
        }

        if (a == b) return a;

        for (int j = LOG - 1; j >= 0; j--) {
            if (up[a][j] != up[b][j]) {
                a = up[a][j];
                b = up[b][j];
            }
        }

        return up[a][0];
    }

    public int[] assignEdgeWeights(int[][] edges, int[][] queries) {
        int n = edges.length + 1;

        LOG = 17;
        while ((1 << LOG) <= n) LOG++;

        graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] e : edges) {
            int u = e[0];
            int v = e[1];

            graph[u].add(v);
            graph[v].add(u);
        }

        depth = new int[n + 1];
        up = new int[n + 1][LOG];

        dfs(1, 1);

        int[] pow2 = new int[n + 1];
        pow2[0] = 1;

        for (int i = 1; i <= n; i++) {
            pow2[i] = (int)((long)pow2[i - 1] * 2 % MOD);
        }

        int[] ans = new int[queries.length];

        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0];
            int v = queries[i][1];

            int ancestor = lca(u, v);

            int dist = depth[u] + depth[v] - 2 * depth[ancestor];

            ans[i] = (dist == 0) ? 0 : pow2[dist - 1];
        }

        return ans;
    }
}




class Solution {
public:
    static const int MOD = 1000000007;

    vector<int> depth;
    vector<vector<int>> up;
    vector<vector<int>> graph;
    int LOG;

    void dfs(int node, int parent) {
        up[node][0] = parent;

        for (int j = 1; j < LOG; j++) {
            up[node][j] = up[up[node][j - 1]][j - 1];
        }

        for (int next : graph[node]) {
            if (next == parent) continue;

            depth[next] = depth[node] + 1;
            dfs(next, node);
        }
    }

    int lca(int a, int b) {
        if (depth[a] < depth[b]) swap(a, b);

        int diff = depth[a] - depth[b];

        for (int j = LOG - 1; j >= 0; j--) {
            if ((diff >> j) & 1) {
                a = up[a][j];
            }
        }

        if (a == b) return a;

        for (int j = LOG - 1; j >= 0; j--) {
            if (up[a][j] != up[b][j]) {
                a = up[a][j];
                b = up[b][j];
            }
        }

        return up[a][0];
    }

    vector<int> assignEdgeWeights(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = edges.size() + 1;

        LOG = 17;
        while ((1 << LOG) <= n) LOG++;

        graph.assign(n + 1, {});
        for (auto &e : edges) {
            int u = e[0];
            int v = e[1];

            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        depth.assign(n + 1, 0);
        up.assign(n + 1, vector<int>(LOG, 1));

        dfs(1, 1);

        vector<int> pow2(n + 1, 1);
        for (int i = 1; i <= n; i++) {
            pow2[i] = (long long)pow2[i - 1] * 2 % MOD;
        }

        vector<int> ans;

        for (auto &q : queries) {
            int u = q[0];
            int v = q[1];

            int ancestor = lca(u, v);

            int dist = depth[u] + depth[v] - 2 * depth[ancestor];

            if (dist == 0) {
                ans.push_back(0);
            } else {
                ans.push_back(pow2[dist - 1]);
            }
        }

        return ans;
    }
};


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 1000000007

        n = len(edges) + 1

        LOG = 1
        while (1 << LOG) <= n:
            LOG += 1

        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        depth = [0] * (n + 1)
        up = [[1] * LOG for _ in range(n + 1)]

        def dfs(node: int, parent: int) -> None:
            up[node][0] = parent

            for j in range(1, LOG):
                up[node][j] = up[up[node][j - 1]][j - 1]

            for nxt in graph[node]:
                if nxt == parent:
                    continue

                depth[nxt] = depth[node] + 1
                dfs(nxt, node)

        dfs(1, 1)

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]

            for j in range(LOG - 1, -1, -1):
                if (diff >> j) & 1:
                    a = up[a][j]

            if a == b:
                return a

            for j in range(LOG - 1, -1, -1):
                if up[a][j] != up[b][j]:
                    a = up[a][j]
                    b = up[b][j]

            return up[a][0]

        pow2 = [1] * (n + 1)

        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = []

        for u, v in queries:
            ancestor = lca(u, v)

            dist = depth[u] + depth[v] - 2 * depth[ancestor]

            if dist == 0:
                ans.append(0)
            else:
                ans.append(pow2[dist - 1])

        return ans
		


func assignEdgeWeights(edges [][]int) int {
	n := len(edges) + 1
	graph := make([][]int, n+1)
	
	for _, e := range edges {
		graph[e[0]] = append(graph[e[0]], e[1])
		graph[e[1]] = append(graph[e[1]], e[0])
	}

	var dfs func(int, int) int
	dfs = func(node, prev int) int {
		dist := 0
		for _, g := range graph[node] {
			if g != prev {
				dist = max(dist, dfs(g, node)+1)
			}
		}
		return dist
	}

	return pow(2, dfs(1, 0)-1)
}

func pow(base, exp int) int {
	const mod = 1_000_000_007
	res := 1
	
	for exp > 0 {
		if exp%2 > 0 {
			res = res * base % mod
		}
		base = base * base % mod
		exp /= 2
	}
	
	return res
}




struct Solution {
    static constexpr unsigned assignEdgeWeights(const vector<vector<int>>& edges) {
        static constexpr unsigned mod = 1000000007;

        unsigned size = edges.size() + 1u;
        auto arr = make_unique<unsigned[]>(size * 3u);

        unsigned* const cnt = arr.get();
        unsigned* const sum = cnt + size;
        unsigned* right = sum + size;
        const unsigned* left = right;

        for (span<const int> e : edges) {
            unsigned u = e[0] - 1u;
            unsigned v = e[1] - 1u;

            ++cnt[u];
            ++cnt[v];

            sum[u] ^= v;
            sum[v] ^= u;
        }

        for (unsigned i = 1; i != size; ++i)
            if (cnt[i] == 1u)
                *right++ = i;

        unsigned res = 1;

        while (left != right) {
            span<const unsigned> curr(left, right);
            left = right;

            for (unsigned v : curr) {
                unsigned p = sum[v];

                if (p) {
                    sum[p] ^= v;

                    if (--cnt[p] == 1u)
                        *right++ = p;
                }
            }

            res %= mod;
            res *= 2u;
        }

        return res / 2u;
    }
};


class Solution {
    static constexpr int mod = 1000000007;

    long long pow(long long base, int exp) {
        long long res = 1;

        while (exp) {
            if (exp & 1)
                res = res * base % mod;

            base = base * base % mod;
            exp >>= 1;
        }

        return res;
    }

public:
    int assignEdgeWeights(vector<vector<int>>& edges) {
        int size = edges.size() + 1;
        vector<vector<int>> arr(size + 1);

        for (auto& e : edges) {
            arr[e[0]].push_back(e[1]);
            arr[e[1]].push_back(e[0]);
        }

        auto dfs = [&](this auto&& dfs, int node, int prev) -> int {
            int res = 0;

            for (auto& x : arr[node])
                if (x != prev)
                    res = max(res, dfs(x, node) + 1);

            return res;
        };

        return pow(2, dfs(1, 0) - 1);
    }
};

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = 1_000_000_007
        n = len(edges) + 1
        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node: int, prev: int) -> int:
            d = 0
            for c in graph[node]:
                if c != prev:
                    d = max(d, dfs(c, node) + 1)
            return d

        return pow(2, dfs(1, 0) - 1, mod)


class Solution {
  public:
    bool canSeatAllPeople(int k, vector<int> &seats) {
        // code here
        int n=seats.size();
        for(int i=1; i<n; i++){
            if(seats[i]==1 && seats[i-1]==1) return 0;
        }
        if(k==1 && n==1){
            return seats[0]==0?1:0;
        } 

        int cnt=0;
        for(int i=0; i<n; i++){
            if(i==0 && seats[i]==0){
                if(i+1<n && seats[i+1]==0){
                    seats[i]=1;
                    cnt++;
                }
            }else if(i==n-1 && seats[i]==0){
                if(i-1>=0 && seats[i-1]==0){
                    seats[i]=1;
                    cnt++;
                }
            }else{
                if(seats[i-1]==0 && seats[i+1]==0 && seats[i]==0){
                    seats[i]=1;
                    cnt++;
                }
            }
        }

        if(cnt>=k) return true;
        return false;
    }
};




class Solution {
  public:
    bool canSeatAllPeople(int k, vector<int> &seats) {
        // code here
        int n=seats.size();
        for(int i=1; i<n; i++){
            if(seats[i]==1 && seats[i-1]==1) return 0;
        }
        if(k==1 && n==1){
            return seats[0]==0?1:0;
        } 

        int cnt=0;
        for(int i=0; i<n; i++){
            if(i==0 && seats[i]==0){
                if(i+1<n && seats[i+1]==0){
                    seats[i]=1;
                    cnt++;
                }
            }else if(i==n-1 && seats[i]==0){
                if(i-1>=0 && seats[i-1]==0){
                    seats[i]=1;
                    cnt++;
                }
            }else{
                if(seats[i-1]==0 && seats[i+1]==0 && seats[i]==0){
                    seats[i]=1;
                    cnt++;
                }
            }
        }

        if(cnt>=k) return true;
        return false;
    }
};


class Solution:
    def maxTotalValue(self, A: List[int], k: int) -> int:
        gMin = gMax = A[0]

        for n in A:
            gMin = min(gMin, n)
            gMax = max(gMax, n)

        return (gMax - gMin) * k


class Solution {
  public:
    bool canSeatAllPeople(int k, vector<int> &seats) {
        // code here
        int n=seats.size();
        for(int i=1; i<n; i++){
            if(seats[i]==1 && seats[i-1]==1) return 0;
        }
        if(k==1 && n==1){
            return seats[0]==0?1:0;
        } 

        int cnt=0;
        for(int i=0; i<n; i++){
            if(i==0 && seats[i]==0){
                if(i+1<n && seats[i+1]==0){
                    seats[i]=1;
                    cnt++;
                }
            }else if(i==n-1 && seats[i]==0){
                if(i-1>=0 && seats[i-1]==0){
                    seats[i]=1;
                    cnt++;
                }
            }else{
                if(seats[i-1]==0 && seats[i+1]==0 && seats[i]==0){
                    seats[i]=1;
                    cnt++;
                }
            }
        }

        if(cnt>=k) return true;
        return false;
    }
};

class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int n = nums.length;
        int[] ans = new int[n];

        int left = 0;
        int right = n - 1;

        int i = 0;
        int j = n - 1;

        while (i < n) {
            if (nums[i] < pivot) {
                ans[left++] = nums[i];
            }

            if (nums[j] > pivot) {
                ans[right--] = nums[j];
            }

            i++;
            j--;
        }

        // Remaining positions contain pivot
        while (left <= right) {
            ans[left++] = pivot;
        }

        return ans;
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#pragma optimize("O3, unroll-loops")
static int* pivotArray(int* nums, int n, int pivot, int* returnSize) {
    *returnSize=n;
    if (n==1) return nums;
    int R[n];
    int l=0, r=0;
    for(int i=0; i<n; i++){
        const int x=nums[i];
        nums[l]=R[r]=x;
        l+=(x<pivot);
        r+=(x>pivot);
    }
    int m=n-r-l;
    for(int i=l; i<l+m; i++) nums[i]=pivot;
    for(int j=0; j<r; j++) nums[l+m+j]=R[j];
    return nums;
}

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        if n==1: return nums
        R=[]
        l, m=0, 0
        for x in nums:
            if x<pivot:
                nums[l]=x
                l+=1
            elif x>pivot:
                R.append(x)
            else:
                m+=1
        return nums[:l]+[pivot]*m+R
        




class Solution {
public:
    static vector<int> pivotArray(vector<int>& nums, int pivot) {
        int n=nums.size();
        if (n==1) return nums;
        int R[n];
        int l=0, r=0;
        for(int x: nums){
            nums[l]=R[r]=x;
            l+=(x<pivot);
            r+=(x>pivot);
        }
        int m=n-r-l;
        auto it_m=nums.begin()+l;
        fill(it_m, it_m+m, pivot);
        copy(R, R+r, it_m+m);
        return nums;
    }
};


class Solution {
public:
    TreeNode* createBinaryTree(vector<vector<int>>& A) {
        unordered_map<int, TreeNode*> nodes;
        nodes.reserve(A.size() + 1);
        int root = 0;

        for (auto& d : A) {
            int x = d[0], y = d[1], isLeft = d[2];
            if (!nodes.contains(x)) {
                nodes[x] = new TreeNode(x);
                root ^= x;
            }
            if (!nodes.contains(y)) {
                nodes[y] = new TreeNode(y);
                root ^= y;
            }

            if (isLeft)
                nodes[x]->left = nodes[y];
            else
                nodes[x]->right = nodes[y];
            root ^= y;
        }

        return nodes[root];
    }
};


class Solution {
    public TreeNode createBinaryTree(int[][] A) {
        Map<Integer, TreeNode> nodes = new HashMap<>(A.length + 1, 1);
        int root = 0;

        for (int[] d : A) {
            int x = d[0], y = d[1];
            if (!nodes.containsKey(x)) {
                nodes.put(x, new TreeNode(x));
                root ^= x;
            }
            if (!nodes.containsKey(y)) {
                nodes.put(y, new TreeNode(y));
                root ^= y;
            }
            if (d[2] == 1) {
                nodes.get(x).left = nodes.get(y);
            } else {
                nodes.get(x).right = nodes.get(y);
            }
            root ^= y;
        }

        return nodes.get(root);
    }
}


func createBinaryTree(A [][]int) *TreeNode {
	nodes := make(map[int]*TreeNode, len(A)+1)
	root := 0

	for _, d := range A {
		x, y := d[0], d[1]
		if nodes[x] == nil {
			nodes[x] = &TreeNode{Val: x}
			root ^= x
		}
		if nodes[y] == nil {
			nodes[y] = &TreeNode{Val: y}
			root ^= y
		}
		if d[2] == 1 {
			nodes[x].Left = nodes[y]
		} else {
			nodes[x].Right = nodes[y]
		}
		root ^= y
	}

	return nodes[root]
}




class Solution {
public:
    TreeNode* createBinaryTree(vector<vector<int>>& A) {
        unordered_map<int, TreeNode*> nodes;
        nodes.reserve(A.size() + 1);
        int root = 0;

        for (auto& d : A) {
            int x = d[0], y = d[1], isLeft = d[2];
            if (!nodes.contains(x)) {
                nodes[x] = new TreeNode(x);
                root ^= x;
            }
            if (!nodes.contains(y)) {
                nodes[y] = new TreeNode(y);
                root ^= y;
            }

            if (isLeft)
                nodes[x]->left = nodes[y];
            else
                nodes[x]->right = nodes[y];
            root ^= y;
        }

        return nodes[root];
    }
};


class Solution:
    def createBinaryTree(self, A: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        root = 0

        for x, y, is_left in A:
            if x not in nodes:
                nodes[x] = TreeNode(x)
                root ^= x
            if y not in nodes:
                nodes[y] = TreeNode(y)
                root ^= y
            if is_left:
                nodes[x].left = nodes[y]
            else:
                nodes[x].right = nodes[y]
            root ^= y

        return nodes[root]


using ll = long long;
class Solution {
    static inline int waves[570];
    static inline bool init = []() {
        int j = 0;
        for (int i = 0; i < 1000; i++) {
            int r = i % 10;
            int m = (i / 10) % 10;
            int l = (i / 100) % 10;
            if ((m > max(l, r)) | (m < min(l, r)))
                waves[j++] = i;
        }
        return 0;
    }();

public:
    ll totalWaviness(ll A, ll B) { return waveCount(B) - waveCount(A - 1); }

private:
    ll waveCount(ll num) {
        if (num < 100) return 0;            
        return accumulate(begin(waves), end(waves), 0LL, [&](ll a, int p) {
            return a + countWays(num, p);
        });
    }

    ll countWays(ll num, int pattern) {
        ll t = pattern < 100;
        ll count = 0, mult = 1;

        for (int i = 0; mult * 100 <= num; i++) {
            ll pre = num / (mult * 1000);
            ll cur = (num / mult) % 1000;
            ll suf = num % mult;
            ll ways = 0;

            if (cur > pattern)
                ways = pre - t + 1;
            else if (cur == pattern) {
                ways = max(0LL, pre - t);
                count += suf + 1;
            } else
                ways = max(0LL, pre - t);
            count += ways * mult;
            mult *= 10;
        }

        return count;
    }
};


const { floor, max, min } = Math;

const waves = (() => {
    const arr = [];
    for (let i = 0; i < 1000; i++) {
        const r = i % 10;
        const m = floor(i / 10) % 10;
        const l = floor(i / 100) % 10;
        if ((m > max(l, r)) | (m < min(l, r)))
            arr.push(i);
    }
    return arr;
})();


const totalWaviness = (A, B) => waveCount(B) - waveCount(A - 1);

const waveCount = num => {
    if (num < 100) return 0;
    return waves.reduce((a, c) => a + countWays(num, c), 0);
};

const countWays = (num, pattern) => {
    const type = pattern < 100;
    let count = 0;
    let mult = 1;

    for (let i = 0; mult * 100 <= num; i++) {
        const pre = floor(num / (mult * 1000));
        const cur = floor(num / mult) % 1000;
        const suf = num % mult;

        const ways = max(0, pre - type + (cur > pattern));
        const edge = (cur === pattern) * (suf + 1);

        count += ways * mult + edge;
        mult *= 10;
    }

    return count;
};




class Solution:
    waves = []
    for i in range(1000):
        r = i % 10
        m = (i // 10) % 10
        l = (i // 100) % 10
        if (m > max(l, r)) | (m < min(l, r)):
            waves.append(i)

    def totalWaviness(self, A: int, B: int) -> int:
        return self.waveCount(B) - self.waveCount(A - 1)

    def waveCount(self, num):
        if num < 100: return 0
        return sum(self.countWays(num, p) for p in self.waves)

    def countWays(self, num, pattern):
        s = str(num)
        n = len(s)
        t = pattern < 100
        count = 0
        for i in range(n - 2):
            pre = int(s[:i] or 0)
            cur = int(s[i:i+3])
            suf = int(s[i+3:] or 0)
            mult = 10 ** (n - i - 3)
            ways = 0

            if cur > pattern:
                ways = pre - t + 1
            elif cur == pattern:
                ways = max(0, pre - t)
                count += suf + 1                
            else:
                ways = max(0, pre - t)
            count += ways * mult

        return count
const { floor, max, min } = Math;

const MAX = 100001;
const dp = new Int32Array(MAX);
const pref = new Int32Array(MAX);

for (let i = 100; i < MAX; i++) {
    const d1 = i % 10;
    const d2 = floor(i / 10) % 10;
    const d3 = floor(i / 100) % 10;

    const isWave = (d2 > max(d3, d1)) | (d2 < min(d3, d1));
    dp[i] = dp[floor(i / 10)] + isWave;
    pref[i] = pref[i - 1] + dp[i];
}

const totalWaviness = (A, B) => pref[B] - pref[A - 1];

class Solution {
private:
    static constexpr int MAX = 100001;
    static inline int dp[MAX], pref[MAX];

    static inline bool init = []() {
        for (int i = 100; i < MAX; i++) {
            int r = i % 10;
            int m = (i / 10) % 10;
            int l = (i / 100) % 10;

            bool isWave = (m > max(l, r)) | (m < min(l, r));
            dp[i] = dp[i / 10] + isWave;
            pref[i] = pref[i - 1] + dp[i];
        }
        return 0;
    }();

public:
    int totalWaviness(int A, int B) { return pref[B] - pref[A - 1]; }
};

class Solution:
    MAX = 100001
    dp = [0] * MAX
    pref = [0] * MAX

    for i in range(100, MAX):
        r = i % 10
        m = (i // 10) % 10
        l = (i // 100) % 10

        isWave = m > max(l, r) or m < min(l, r)
        dp[i] = dp[i // 10] + int(isWave)
        pref[i] = pref[i - 1] + dp[i]

    def totalWaviness(self, A: int, B: int) -> int:
        return self.pref[B] - self.pref[A - 1]



class Solution {
    static inline int MAX = 300005;
public:
    int earliestFinishTime(vector<int>& la, vector<int>& lb, vector<int>& wa, vector<int>& wb) {
        int l = MAX, w = MAX, minL = MAX, minW = MAX;
        int n = la.size(), m = wa.size();

        for (int i = 0; i < n; i++)
            l = min(l, la[i] + lb[i]);

        for (int i = 0; i < m; i++) {
            w = min(w, wa[i] + wb[i]);
            minL = min(minL, max(wa[i], l) + wb[i]);
        }

        for (int i = 0; i < n; i++)
            minW = min(minW, max(la[i], w) + lb[i]);

        return min(minW, minL);
    }
};


class Solution:
    def earliestFinishTime(
        self, la: list[int], lb: list[int], wa: list[int], wb: list[int]
    ) -> int:
        MAX = 300005
        l = w = minL = minW = MAX
        n, m = len(la), len(wa)

        for i in range(n):
            l = min(l, la[i] + lb[i])

        for i in range(m):
            w = min(w, wa[i] + wb[i])
            minL = min(minL, max(wa[i], l) + wb[i])

        for i in range(n):
            minW = min(minW, max(la[i], w) + lb[i])

        return min(minW, minL)

import { useState } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { GraduationCap, Code, Layers, Sparkles, BookOpen, ChevronRight, Check } from 'lucide-react';
import { education, skills } from '../data';

export default function About() {
  const [skillFilter, setSkillFilter] = useState<'all' | 'programming' | 'ml' | 'data' | 'other'>('all');

  const categories = [
    { id: 'all', label: 'All Skillsets' },
    { id: 'programming', label: 'Languages & Tools' },
    { id: 'ml', label: 'Machine Learning' },
    { id: 'data', label: 'Data Handling / Viz' },
    { id: 'other', label: 'Others' }
  ];

  const filteredSkills = skills.filter(
    (skill) => skillFilter === 'all' || skill.category === skillFilter
  );

  return (
    <section
      id="about"
      className="py-24 bg-white dark:bg-[#020617] border-b border-slate-200/55 dark:border-white/5 relative"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        
        {/* Section Header */}
        <div className="max-w-3xl mx-auto text-center mb-16">
          <div className="inline-flex items-center space-x-2 bg-cyan-50 dark:bg-cyan-950/30 px-3 py-1 rounded-full border border-cyan-200/30 mb-3">
            <Sparkles className="h-3.5 w-3.5 text-cyan-500" />
            <span className="text-xs font-mono font-semibold text-cyan-700 dark:text-cyan-400 uppercase tracking-widest">
              Profile Details
            </span>
          </div>
          <h2 className="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight">
            Academic Journey & Skill Index
          </h2>
          <p className="mt-4 text-base text-slate-500 dark:text-slate-400">
            A comprehensive overview of my academic credentials in Artificial Intelligence & Machine Learning along with specialized software development sets.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
          
          {/* Column 1: Education Timeline & History */}
          <div id="education-academic-timeline" className="lg:col-span-6 space-y-8">
            <div className="flex items-center space-x-3 mb-4">
              <div className="bg-cyan-500/10 dark:bg-cyan-500/10 text-cyan-600 dark:text-cyan-400 p-2.5 rounded-xl border border-cyan-500/10">
                <GraduationCap className="h-6 w-6" />
              </div>
              <h3 className="text-xl font-extrabold text-slate-900 dark:text-white">
                Education Milestones
              </h3>
            </div>

            <div className="relative pl-6 border-l-2 border-slate-200 dark:border-slate-800 space-y-8">
              {education.map((edu, idx) => (
                <motion.div
                  key={edu.id}
                  id={`edu-item-${idx}`}
                  initial={{ opacity: 0, x: -15 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: idx * 0.1 }}
                  className="relative group"
                >
                  {/* Decorative bullet node */}
                  <div className="absolute -left-[31px] top-1.5 h-4 w-4 rounded-full border-2 border-cyan-500 bg-white dark:bg-[#020617] group-hover:bg-cyan-500 transition-colors duration-300 shadow-sm" />
                  
                  <div className="bg-slate-50/50 dark:bg-slate-900/40 p-5 rounded-2xl border border-slate-200/40 dark:border-white/5 hover:border-cyan-500/30 transition-all duration-300 shadow-sm">
                    <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-1.5 mb-2">
                      <span className="text-xs font-mono font-semibold text-cyan-600 dark:text-cyan-400">
                        {edu.timeline}
                      </span>
                      <span className="inline-flex self-start sm:self-auto px-2.5 py-0.5 rounded-full text-xs font-semibold bg-cyan-100 dark:bg-cyan-950/40 text-cyan-700 dark:text-cyan-400 border border-cyan-200/20">
                        {edu.gradeLabel}: {edu.grade}
                      </span>
                    </div>
                    
                    <h4 className="text-base font-bold text-slate-900 dark:text-white group-hover:text-cyan-500 dark:group-hover:text-cyan-400 transition-colors">
                      {edu.degree}
                    </h4>
                    <p className="text-xs text-slate-500 dark:text-slate-400 font-medium">
                      {edu.institution}
                    </p>
                    
                    {edu.details && (
                      <p className="mt-2.5 text-xs text-slate-650 dark:text-slate-400 leading-relaxed">
                        {edu.details}
                      </p>
                    )}
                  </div>
                </motion.div>
              ))}
            </div>
          </div>

          {/* Column 2: Technical Skill Deck */}
          <div id="skills-deck" className="lg:col-span-6 space-y-6">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-4">
              <div className="flex items-center space-x-3">
                <div className="bg-cyan-500/10 dark:bg-cyan-500/10 text-cyan-600 dark:text-cyan-400 p-2.5 rounded-xl border border-cyan-500/10">
                  <Code className="h-6 w-6" />
                </div>
                <h3 className="text-xl font-extrabold text-slate-900 dark:text-white">
                  Technical Skill Deck
                </h3>
              </div>
            </div>

            {/* Sub-selector Filter categories tag slider */}
            <div className="flex flex-wrap gap-1.5 p-1 bg-slate-100 dark:bg-slate-900/60 rounded-xl border border-slate-200/60 dark:border-white/5">
              {categories.map((cat) => (
                <button
                  key={cat.id}
                  id={`skill-filter-${cat.id}`}
                  onClick={() => setSkillFilter(cat.id as any)}
                  className={`px-3 py-1.5 rounded-lg text-xs font-medium tracking-wide transition-all duration-200 cursor-pointer ${
                    skillFilter === cat.id
                      ? 'bg-white dark:bg-slate-800 text-cyan-600 dark:text-cyan-400 shadow-sm font-semibold'
                      : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                  }`}
                >
                  {cat.label}
                </button>
              ))}
            </div>

            {/* Proficiencies Bars list layout */}
            <div id="skills-bars-grid" className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <AnimatePresence mode="popLayout">
                {filteredSkills.map((skill) => (
                  <motion.div
                    layout
                    key={skill.name}
                    initial={{ opacity: 0, scale: 0.9 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0, scale: 0.9 }}
                    transition={{ duration: 0.25 }}
                    className="p-4 bg-slate-50/50 dark:bg-slate-900/20 border border-slate-200/40 dark:border-white/5 rounded-2xl flex flex-col justify-between hover:border-cyan-500/20 hover:bg-slate-150/20 dark:hover:bg-slate-900/30 transition-all shadow-sm"
                  >
                    <div className="flex justify-between items-center mb-2">
                      <span className="text-xs font-bold text-slate-800 dark:text-slate-200">
                        {skill.name}
                      </span>
                      <span className="text-[10px] font-mono leading-none bg-slate-200/50 dark:bg-slate-800 px-1.5 py-1 rounded text-slate-600 dark:text-slate-400">
                        {skill.level}%
                      </span>
                    </div>

                    {/* Filling line */}
                    <div className="w-full h-2 bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                      <motion.div
                        initial={{ width: 0 }}
                        whileInView={{ width: `${skill.level}%` }}
                        viewport={{ once: true }}
                        transition={{ duration: 0.9, ease: 'easeOut' }}
                        className="h-full bg-gradient-to-r from-cyan-500 to-blue-500 rounded-full"
                      />
                    </div>
                  </motion.div>
                ))}
              </AnimatePresence>
            </div>

            {/* Quick Resume Bullet checklist */}
            <div className="bg-cyan-500/5 dark:bg-cyan-400/5 border border-cyan-500/10 rounded-2xl p-4 mt-6">
              <span className="text-xs font-mono uppercase tracking-widest text-cyan-500 dark:text-cyan-400 font-bold block mb-2">Domain Focus Areas</span>
              <ul className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs text-slate-600 dark:text-slate-400">
                <li className="flex items-center gap-2">
                  <Check className="h-3.5 w-3.5 text-cyan-500 dark:text-cyan-400 shrink-0" />
                  Model Preprocessing pipelines
                </li>
                <li className="flex items-center gap-2">
                  <Check className="h-3.5 w-3.5 text-cyan-500 dark:text-cyan-400 shrink-0" />
                  Supervised Classification Tasks
                </li>
                <li className="flex items-center gap-2">
                  <Check className="h-3.5 w-3.5 text-cyan-500 dark:text-cyan-400 shrink-0" />
                  Visual Analysis Plotting
                </li>
                <li className="flex items-center gap-2">
                  <Check className="h-3.5 w-3.5 text-cyan-505 dark:text-cyan-400 shrink-0" />
                  Desktop App GUI Scripting (Tkinter)
                </li>
              </ul>
            </div>

          </div>

        </div>

      </div>
    </section>
  );
}



import { useState } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { GraduationCap, Code, Layers, Sparkles, BookOpen, ChevronRight, Check } from 'lucide-react';
import { education, skills } from '../data';

export default function About() {
  const [skillFilter, setSkillFilter] = useState<'all' | 'programming' | 'ml' | 'data' | 'other'>('all');

  const categories = [
    { id: 'all', label: 'All Skillsets' },
    { id: 'programming', label: 'Languages & Tools' },
    { id: 'ml', label: 'Machine Learning' },
    { id: 'data', label: 'Data Handling / Viz' },
    { id: 'other', label: 'Others' }
  ];

  const filteredSkills = skills.filter(
    (skill) => skillFilter === 'all' || skill.category === skillFilter
  );

  return (
    <section
      id="about"
      className="py-24 bg-white dark:bg-[#020617] border-b border-slate-200/55 dark:border-white/5 relative"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        
        {/* Section Header */}
        <div className="max-w-3xl mx-auto text-center mb-16">
          <div className="inline-flex items-center space-x-2 bg-cyan-50 dark:bg-cyan-950/30 px-3 py-1 rounded-full border border-cyan-200/30 mb-3">
            <Sparkles className="h-3.5 w-3.5 text-cyan-500" />
            <span className="text-xs font-mono font-semibold text-cyan-700 dark:text-cyan-400 uppercase tracking-widest">
              Profile Details
            </span>
          </div>
          <h2 className="text-3xl sm:text-4xl font-extrabold text-slate-900 dark:text-white tracking-tight">
            Academic Journey & Skill Index
          </h2>
          <p className="mt-4 text-base text-slate-500 dark:text-slate-400">
            A comprehensive overview of my academic credentials in Artificial Intelligence & Machine Learning along with specialized software development sets.
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start">
          
          {/* Column 1: Education Timeline & History */}
          <div id="education-academic-timeline" className="lg:col-span-6 space-y-8">
            <div className="flex items-center space-x-3 mb-4">
              <div className="bg-cyan-500/10 dark:bg-cyan-500/10 text-cyan-600 dark:text-cyan-400 p-2.5 rounded-xl border border-cyan-500/10">
                <GraduationCap className="h-6 w-6" />
              </div>
              <h3 className="text-xl font-extrabold text-slate-900 dark:text-white">
                Education Milestones
              </h3>
            </div>

            <div className="relative pl-6 border-l-2 border-slate-200 dark:border-slate-800 space-y-8">
              {education.map((edu, idx) => (
                <motion.div
                  key={edu.id}
                  id={`edu-item-${idx}`}
                  initial={{ opacity: 0, x: -15 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: idx * 0.1 }}
                  className="relative group"
                >
                  {/* Decorative bullet node */}
                  <div className="absolute -left-[31px] top-1.5 h-4 w-4 rounded-full border-2 border-cyan-500 bg-white dark:bg-[#020617] group-hover:bg-cyan-500 transition-colors duration-300 shadow-sm" />
                  
                  <div className="bg-slate-50/50 dark:bg-slate-900/40 p-5 rounded-2xl border border-slate-200/40 dark:border-white/5 hover:border-cyan-500/30 transition-all duration-300 shadow-sm">
                    <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-1.5 mb-2">
                      <span className="text-xs font-mono font-semibold text-cyan-600 dark:text-cyan-400">
                        {edu.timeline}
                      </span>
                      <span className="inline-flex self-start sm:self-auto px-2.5 py-0.5 rounded-full text-xs font-semibold bg-cyan-100 dark:bg-cyan-950/40 text-cyan-700 dark:text-cyan-400 border border-cyan-200/20">
                        {edu.gradeLabel}: {edu.grade}
                      </span>
                    </div>
                    
                    <h4 className="text-base font-bold text-slate-900 dark:text-white group-hover:text-cyan-500 dark:group-hover:text-cyan-400 transition-colors">
                      {edu.degree}
                    </h4>
                    <p className="text-xs text-slate-500 dark:text-slate-400 font-medium">
                      {edu.institution}
                    </p>
                    
                    {edu.details && (
                      <p className="mt-2.5 text-xs text-slate-650 dark:text-slate-400 leading-relaxed">
                        {edu.details}
                      </p>
                    )}
                  </div>
                </motion.div>
              ))}
            </div>
          </div>

          {/* Column 2: Technical Skill Deck */}
          <div id="skills-deck" className="lg:col-span-6 space-y-6">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-4">
              <div className="flex items-center space-x-3">
                <div className="bg-cyan-500/10 dark:bg-cyan-500/10 text-cyan-600 dark:text-cyan-400 p-2.5 rounded-xl border border-cyan-500/10">
                  <Code className="h-6 w-6" />
                </div>
                <h3 className="text-xl font-extrabold text-slate-900 dark:text-white">
                  Technical Skill Deck
                </h3>
              </div>
            </div>

            {/* Sub-selector Filter categories tag slider */}
            <div className="flex flex-wrap gap-1.5 p-1 bg-slate-100 dark:bg-slate-900/60 rounded-xl border border-slate-200/60 dark:border-white/5">
              {categories.map((cat) => (
                <button
                  key={cat.id}
                  id={`skill-filter-${cat.id}`}
                  onClick={() => setSkillFilter(cat.id as any)}
                  className={`px-3 py-1.5 rounded-lg text-xs font-medium tracking-wide transition-all duration-200 cursor-pointer ${
                    skillFilter === cat.id
                      ? 'bg-white dark:bg-slate-800 text-cyan-600 dark:text-cyan-400 shadow-sm font-semibold'
                      : 'text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white'
                  }`}
                >
                  {cat.label}
                </button>
              ))}
            </div>

            {/* Proficiencies Bars list layout */}
            <div id="skills-bars-grid" className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <AnimatePresence mode="popLayout">
                {filteredSkills.map((skill) => (
                  <motion.div
                    layout
                    key={skill.name}
                    initial={{ opacity: 0, scale: 0.9 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0, scale: 0.9 }}
                    transition={{ duration: 0.25 }}
                    className="p-4 bg-slate-50/50 dark:bg-slate-900/20 border border-slate-200/40 dark:border-white/5 rounded-2xl flex flex-col justify-between hover:border-cyan-500/20 hover:bg-slate-150/20 dark:hover:bg-slate-900/30 transition-all shadow-sm"
                  >
                    <div className="flex justify-between items-center mb-2">
                      <span className="text-xs font-bold text-slate-800 dark:text-slate-200">
                        {skill.name}
                      </span>
                      <span className="text-[10px] font-mono leading-none bg-slate-200/50 dark:bg-slate-800 px-1.5 py-1 rounded text-slate-600 dark:text-slate-400">
                        {skill.level}%
                      </span>
                    </div>

                    {/* Filling line */}
                    <div className="w-full h-2 bg-slate-200 dark:bg-slate-800 rounded-full overflow-hidden">
                      <motion.div
                        initial={{ width: 0 }}
                        whileInView={{ width: `${skill.level}%` }}
                        viewport={{ once: true }}
                        transition={{ duration: 0.9, ease: 'easeOut' }}
                        className="h-full bg-gradient-to-r from-cyan-500 to-blue-500 rounded-full"
                      />
                    </div>
                  </motion.div>
                ))}
              </AnimatePresence>
            </div>

            {/* Quick Resume Bullet checklist */}
            <div className="bg-cyan-500/5 dark:bg-cyan-400/5 border border-cyan-500/10 rounded-2xl p-4 mt-6">
              <span className="text-xs font-mono uppercase tracking-widest text-cyan-500 dark:text-cyan-400 font-bold block mb-2">Domain Focus Areas</span>
              <ul className="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs text-slate-600 dark:text-slate-400">
                <li className="flex items-center gap-2">
                  <Check className="h-3.5 w-3.5 text-cyan-500 dark:text-cyan-400 shrink-0" />
                  Model Preprocessing pipelines
                </li>
                <li className="flex items-center gap-2">
                  <Check className="h-3.5 w-3.5 text-cyan-500 dark:text-cyan-400 shrink-0" />
                  Supervised Classification Tasks
                </li>
                <li className="flex items-center gap-2">
                  <Check className="h-3.5 w-3.5 text-cyan-500 dark:text-cyan-400 shrink-0" />
                  Visual Analysis Plotting
                </li>
                <li className="flex items-center gap-2">
                  <Check className="h-3.5 w-3.5 text-cyan-505 dark:text-cyan-400 shrink-0" />
                  Desktop App GUI Scripting (Tkinter)
                </li>
              </ul>
            </div>

          </div>

        </div>

      </div>
    </section>
  );
}


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        total = 0

        i = len(cost) - 1

        while i >= 0:
            total += cost[i]
            if i - 1 >= 0:
                total += cost[i - 1]

            i -= 3

        return total

class Solution {
  public:
    void replaceElements(vector<int>& arr) {
        // code here
        int n = (int)arr.size();
        
        arr[0] = arr[0] ^ arr[1];
        int s = 0 ;
        s = s ^ arr[0];
        for(int i = 1;(i+1)<n;i++)
        {
            arr[i] = (arr[i] ^ s ^ arr[i+1]);
            s^=arr[i];
        }
        
        arr[n-1] = s ;
        
        
    }
};


class Solution {
public:

    vector<int> seg;
    const int MAXX = 50000;

    void update(int node, int l, int r, int idx, int val) {
        if (l == r) {
            seg[node] = val;
            return;
        }

        int mid = (l + r) / 2;

        if (idx <= mid)
            update(2 * node, l, mid, idx, val);
        else
            update(2 * node + 1, mid + 1, r, idx, val);

        seg[node] = max(seg[2 * node], seg[2 * node + 1]);
    }

    int query(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l)
            return 0;

        if (ql <= l && r <= qr)
            return seg[node];

        int mid = (l + r) / 2;

        return max(
            query(2 * node, l, mid, ql, qr),
            query(2 * node + 1, mid + 1, r, ql, qr)
        );
    }

    vector<bool> getResults(vector<vector<int>>& queries) {

        seg.resize(4 * (MAXX + 1), 0);

        set<int> obstacles;
        obstacles.insert(0);

        // Build final obstacle configuration
        for (auto &q : queries) {
            if (q[0] == 1) obstacles.insert(q[1]);
        }

        vector<int> pos(obstacles.begin(), obstacles.end());
        // at pos[i] we have a gap of (pos[i] - pos[i - 1]) which we are storing
        // in the segment tree
        for (int i = 1; i < (int)pos.size(); i++) {
            update(1,0,MAXX,pos[i],pos[i] - pos[i - 1]);
        }

        vector<bool> ans;

        for (int i = (int)queries.size() - 1; i >= 0; i--) {

            if (queries[i][0] == 2) {

                int x = queries[i][1];
                int sz = queries[i][2];
                // find a prev obstacle lesser than x, then we can fit the block
                //before prev or between prev to x
                auto it = prev(obstacles.upper_bound(x));

                int prevObstacle = *it;
                int best = query(1,0,MAXX,0,prevObstacle);

                best = max(best, x - prevObstacle);
                ans.push_back(best >= sz);
            }
            else {

                int x = queries[i][1]; // so we now remove x obstacle
                auto it = obstacles.find(x);
                int leftPos = *prev(it); //left of x

                update(1,0,MAXX,x,0); // update gap at x to 0 or remove gap ending at x

                auto rightIt = next(it);

                if (rightIt != obstacles.end()) {
                    int rightPos = *rightIt;
                    // merging the interval from leftpos to rightpos as one single gap
                    update(1,0,MAXX,rightPos,rightPos - leftPos);
                }

                obstacles.erase(it);
            }
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};


class Solution:

    MAXX = 50000

    def __init__(self):
        self.seg = [0] * (4 * (self.MAXX + 1))

    def update(self, node, l, r, idx, val):
        if l == r:
            self.seg[node] = val
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(2 * node, l, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, val)

        self.seg[node] = max(
            self.seg[2 * node],
            self.seg[2 * node + 1]
        )

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return 0

        if ql <= l and r <= qr:
            return self.seg[node]

        mid = (l + r) // 2

        return max(
            self.query(2 * node, l, mid, ql, qr),
            self.query(2 * node + 1, mid + 1, r, ql, qr)
        )

    def getResults(self, queries: List[List[int]]) -> List[bool]:
        
        obstacles = SortedSet([0])

        # Build final obstacle configuration
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        pos = list(obstacles)

        # gap[pos[i]] = pos[i] - pos[i-1]
        for i in range(1, len(pos)):
            self.update(1,0,self.MAXX,pos[i],pos[i] - pos[i - 1])

        ans = []

        for i in range(len(queries) - 1, -1, -1):

            if queries[i][0] == 2:

                x = queries[i][1]
                sz = queries[i][2]

                idx = obstacles.bisect_right(x) - 1
                prev_obstacle = obstacles[idx]

                best = self.query(1,0,self.MAXX,0,prev_obstacle)
                best = max(best, x - prev_obstacle)

                ans.append(best >= sz)

            else:

                x = queries[i][1]

                idx = obstacles.index(x)
                left_pos = obstacles[idx - 1]

                # remove gap ending at x
                self.update(1,0,self.MAXX,x,0)

                if idx + 1 < len(obstacles):
                    right_pos = obstacles[idx + 1]
                    # merge gaps
                    self.update(1,0,self.MAXX,right_pos,right_pos - left_pos)

                obstacles.remove(x)

        return ans[::-1]
        

class Solution {
    struct TrieNode {
        int children[26];
        int bestLen;
        int bestIdx;
        
        TrieNode() {
            fill(begin(children), end(children), -1);
            bestLen = 1e9;
            bestIdx = 1e9;
        }
    };

public:
    vector<int> stringIndices(vector<string>& wordsContainer, vector<string>& wordsQuery) {
        vector<TrieNode> trie;
        trie.emplace_back();
        
        for (int i = 0; i < wordsContainer.size(); i++) {
            int len = wordsContainer[i].length();
            int curr = 0;
            
            if (len < trie[curr].bestLen || (len == trie[curr].bestLen && i < trie[curr].bestIdx)) {
                trie[curr].bestLen = len;
                trie[curr].bestIdx = i;
            }
            
            for (int j = len - 1; j >= 0; j--) {
                int charIdx = wordsContainer[i][j] - 'a';
                
                if (trie[curr].children[charIdx] == -1) {
                    trie[curr].children[charIdx] = trie.size();
                    trie.emplace_back();
                }
                
                curr = trie[curr].children[charIdx];
                
                if (len < trie[curr].bestLen || (len == trie[curr].bestLen && i < trie[curr].bestIdx)) {
                    trie[curr].bestLen = len;
                    trie[curr].bestIdx = i;
                }
            }
        }
        
        vector<int> ans;
        ans.reserve(wordsQuery.size());
        
        for (const string& query : wordsQuery) {
            int curr = 0;
            int len = query.length();
            
            for (int j = len - 1; j >= 0; j--) {
                int charIdx = query[j] - 'a';
                if (trie[curr].children[charIdx] == -1) {
                    break;
                }
                curr = trie[curr].children[charIdx];
            }
            ans.push_back(trie[curr].bestIdx);
        }
        
        return ans;
    }
}; 

class Solution {
  public:
  void dfs(Node* root,int key,map<int,int> &mp){
      if(!root)return ;
      mp[key]+=root->data;
      dfs(root->left,key-1,mp);
      dfs(root->right,key+1,mp);
  }
    vector<int> verticalSum(Node* root) {
        // code here
        vector<int> ans;
        map<int,int> mp;
        dfs(root,0,mp);
        for(auto i:mp){
            ans.push_back(i.second);
        }
        return ans;
    }
};
 

..... see less

0

Reply
User
Nitin Bhattar
1 hour agoMay 28, 2026 19:51 (GMT +5:30)

Easiest So

class TrieNode:
    __slots__ = ['children', 'bestLen', 'bestIdx']
    
    def __init__(self):
        self.children = {}
        self.bestLen = float('inf')
        self.bestIdx = float('inf')

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        
        for i, word in enumerate(wordsContainer):
            n = len(word)
            curr = root
            
            if n < curr.bestLen or (n == curr.bestLen and i < curr.bestIdx):
                curr.bestLen = n
                curr.bestIdx = i
                
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                
                curr = curr.children[char]
                
                if n < curr.bestLen or (n == curr.bestLen and i < curr.bestIdx):
                    curr.bestLen = n
                    curr.bestIdx = i
                    
        ans = []
        
        for query in wordsQuery:
            curr = root
            
            for char in reversed(query):
                if char not in curr.children:
                    break
                curr = curr.children[char]
            
            ans.append(curr.bestIdx)
            
        return ans

class Solution:
    def canReach(self, s: str, minJ: int, maxJ: int) -> bool:
        n = len(s)

        if int(s[-1]): return False

        dp = [False] * n
        dp[0] = True
        reach, maxR = 0, maxJ

        for i in range(minJ, n):
            if i > maxR: return False

            reach += dp[i - minJ]

            if i > maxJ:
                reach -= dp[i - maxJ - 1]

            if reach and not int(s[i]):
                dp[i] = True
                maxR = i + maxJ

        return reach > 0https://github.com/ctcrahul
        

class Solution:
    def canReach(self, s: str, minJ: int, maxJ: int) -> bool:
        n = len(s)

        if int(s[-1]): return False

        dp = [False] * n
        dp[0] = True
        reach, maxR = 0, maxJ

        for i in range(minJ, n):
            if i > maxR: return False

            reach += dp[i - minJ]

            if i > maxJ:
                reach -= dp[i - maxJ - 1]

            if reach and not int(s[i]):
                dp[i] = True
                maxR = i + maxJ

        return reach > 0

class Solution {
public:
    bool canReach(string s, int minJ, int maxJ) {
        int n = s.length();

        if (s.back() & 1) return false;

        s[0] = 'v';
        int reach = 0, maxR = maxJ;

        for (int i = minJ; i < n; i++) {
            if (i > maxR) return false;

            reach += s[i - minJ] == 'v';
            reach -= (i > maxJ) && s[i - maxJ - 1] == 'v';

            if (reach && (~s[i] & 1)) {
                s[i] = 'v';
                maxR = i + maxJ;
            }
        }

        return reach;
    }
};

class Solution {
public:
    bool canReach(string s, int minJ, int maxJ) {
        int n = s.length();

        if (s.back() & 1) return false;

        s[0] = 'v';
        int reach = 0, maxR = maxJ;

        for (int i = minJ; i < n; i++) {
            if (i > maxR) return false;

            reach += s[i - minJ] == 'v';
            reach -= (i > maxJ) && s[i - maxJ - 1] == 'v';

            if (reach && (~s[i] & 1)) {
                s[i] = 'v';
                maxR = i + maxJ;
            }
        }

        return reach;
    }
};


const canReach = (s, min, max, n = s.length) => {
    if (s.at(-1) & 1) return false;

    const dp = Array(n).fill(false);
    dp[0] = true;
    let reach = 0;
    let maxR = max;

    for (let i = min; i < n; i++) {
        if (i > maxR) return false;

        reach += dp[i - min];
        reach -= (i > max) && dp[i - max - 1];

        if (reach && !(s[i] & 1)) {
            dp[i] = true;
            maxR = i + max;
        }
    }

    return reach;
};

class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        n = len(arr)
        dp = [-1] * n

        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            best = 1

            # Right scan
            for nxt in range(i + 1, min(n, i + d + 1)):
                if arr[nxt] >= arr[i]:
                    break

                best = max(best, 1 + dfs(nxt))

            # Left scan
            for nxt in range(i - 1, max(-1, i - d - 1), -1):
                if arr[nxt] >= arr[i]:
                    break

                best = max(best, 1 + dfs(nxt))

            dp[i] = best
            return dp[i]

        return max(dfs(i) for i in range(n))

class Solution {
public:

int coin(vector<int> &arr) {
    int i = 0;
    int j = arr.size() - 1;
    
    while(i < j) {
        if(arr[i] >= arr[j]) {
            i++;
        }
        else {
            j--;
        }
    }
    
    return arr[i];
}

};


struct Edge{
    int to, nxt=-1;
};

constexpr int V=1000;
constexpr int E=V*2;

Edge POOL[E];
int idx=0;

int adj[V], deg[V];
int dp[V];

int q[V];// for queue holding idx
int front, back;

inline void addEdge(int u, int v){
    POOL[idx]={v, adj[u]};
    adj[u]=idx++;
    deg[v]++;
}
int Stack[V], top=-1;

class Solution {
public:
    static int maxJumps(vector<int>& arr, int d) {
        const int n=arr.size();
        // reset
        idx=0;
        memset(adj, -1, n*sizeof(int));
        memset(deg, 0, n*sizeof(int));
        fill(dp, dp+n, 1);
        // montonone stack
        top=-1;// clear stack
        for(int i=0; i<n; i++){
            const int x=arr[i];
            while(top>-1 && arr[Stack[top]]<x){
                int j=Stack[top--];
                if (i-j<=d) addEdge(j, i);
            }
            Stack[++top]=i;
        }
        top=-1;// clear Stack
        for(int i=n-1; i>=0; i--){
            const int x=arr[i];
            while(top>-1 && arr[Stack[top]]<x){
                int j=Stack[top--];
                if (j-i<=d) addEdge(j, i);
            }
            Stack[++top]=i;
        }

        front=back= 0;// reset for q
        for(int i=0; i<n; i++)// Push i to q if deg[i]=0
            if(deg[i]==0)
                q[back++]=i;

        while(front<back){
            int u=q[front++];
            for(int e=adj[u]; e!=-1; e=POOL[e].nxt){
                int v=POOL[e].to;
                dp[v]=max(dp[v], dp[u]+1);
                if(--deg[v]==0)
                    q[back++]=v;
            }
        }

        return *max_element(dp, dp+n);
    }
};

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int lo = 0, hi = n - 1;

        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] > nums.back()) lo = mid + 1;
            else hi = mid;
        }

        int rot = lo;
        lo = 0, hi = n - 1;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int real = (mid + rot) % n;

            if (nums[real] == target)
                return real;

            if (nums[real] < target) lo = mid + 1;
            else hi = mid - 1;
        }

        return -1;
    }
};


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        rot = bisect_left(nums, True, key=lambda n: n <= nums[-1])
        
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            real = (mid + rot) % n

            if nums[real] == target:
                return real
                
            if nums[real] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1


const search = (nums, target) => {
    let n = nums.length;
    let rot = _.sortedIndexBy(nums, nums.at(-1), c => c <= nums.at(-1));
    let lo = 0, hi = n - 1;

    while (lo <= hi) {
        let mid = (lo + hi) >> 1;
        let real = (mid + rot) % n;

        if (nums[real] === target)
            return real;

        if (nums[real] < target) lo = mid + 1;
        else hi = mid - 1;
    }

    return -1;
};

Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1


class Solution {
  public:
    void replaceElements(vector<int>& arr) {
        // code here
        int n = (int)arr.size();
        
        arr[0] = arr[0] ^ arr[1];
        int s = 0 ;
        s = s ^ arr[0];
        for(int i = 1;(i+1)<n;i++)
        {
            arr[i] = (arr[i] ^ s ^ arr[i+1]);
            s^=arr[i];
        }
        
        arr[n-1] = s ;
        
        
    }
};


class Solution {
public:

    vector<int> seg;
    const int MAXX = 50000;

    void update(int node, int l, int r, int idx, int val) {
        if (l == r) {
            seg[node] = val;
            return;
        }

        int mid = (l + r) / 2;

        if (idx <= mid)
            update(2 * node, l, mid, idx, val);
        else
            update(2 * node + 1, mid + 1, r, idx, val);

        seg[node] = max(seg[2 * node], seg[2 * node + 1]);
    }

    int query(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l)
            return 0;

        if (ql <= l && r <= qr)
            return seg[node];

        int mid = (l + r) / 2;

        return max(
            query(2 * node, l, mid, ql, qr),
            query(2 * node + 1, mid + 1, r, ql, qr)
        );
    }

    vector<bool> getResults(vector<vector<int>>& queries) {

        seg.resize(4 * (MAXX + 1), 0);

        set<int> obstacles;
        obstacles.insert(0);

        // Build final obstacle configuration
        for (auto &q : queries) {
            if (q[0] == 1) obstacles.insert(q[1]);
        }

        vector<int> pos(obstacles.begin(), obstacles.end());
        // at pos[i] we have a gap of (pos[i] - pos[i - 1]) which we are storing
        // in the segment tree
        for (int i = 1; i < (int)pos.size(); i++) {
            update(1,0,MAXX,pos[i],pos[i] - pos[i - 1]);
        }

        vector<bool> ans;

        for (int i = (int)queries.size() - 1; i >= 0; i--) {

            if (queries[i][0] == 2) {

                int x = queries[i][1];
                int sz = queries[i][2];
                // find a prev obstacle lesser than x, then we can fit the block
                //before prev or between prev to x
                auto it = prev(obstacles.upper_bound(x));

                int prevObstacle = *it;
                int best = query(1,0,MAXX,0,prevObstacle);

                best = max(best, x - prevObstacle);
                ans.push_back(best >= sz);
            }
            else {

                int x = queries[i][1]; // so we now remove x obstacle
                auto it = obstacles.find(x);
                int leftPos = *prev(it); //left of x

                update(1,0,MAXX,x,0); // update gap at x to 0 or remove gap ending at x

                auto rightIt = next(it);

                if (rightIt != obstacles.end()) {
                    int rightPos = *rightIt;
                    // merging the interval from leftpos to rightpos as one single gap
                    update(1,0,MAXX,rightPos,rightPos - leftPos);
                }

                obstacles.erase(it);
            }
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};


class Solution:

    MAXX = 50000

    def __init__(self):
        self.seg = [0] * (4 * (self.MAXX + 1))

    def update(self, node, l, r, idx, val):
        if l == r:
            self.seg[node] = val
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(2 * node, l, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, val)

        self.seg[node] = max(
            self.seg[2 * node],
            self.seg[2 * node + 1]
        )

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return 0

        if ql <= l and r <= qr:
            return self.seg[node]

        mid = (l + r) // 2

        return max(
            self.query(2 * node, l, mid, ql, qr),
            self.query(2 * node + 1, mid + 1, r, ql, qr)
        )

    def getResults(self, queries: List[List[int]]) -> List[bool]:
        
        obstacles = SortedSet([0])

        # Build final obstacle configuration
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        pos = list(obstacles)

        # gap[pos[i]] = pos[i] - pos[i-1]
        for i in range(1, len(pos)):
            self.update(1,0,self.MAXX,pos[i],pos[i] - pos[i - 1])

        ans = []

        for i in range(len(queries) - 1, -1, -1):

            if queries[i][0] == 2:

                x = queries[i][1]
                sz = queries[i][2]

                idx = obstacles.bisect_right(x) - 1
                prev_obstacle = obstacles[idx]

                best = self.query(1,0,self.MAXX,0,prev_obstacle)
                best = max(best, x - prev_obstacle)

                ans.append(best >= sz)

            else:

                x = queries[i][1]

                idx = obstacles.index(x)
                left_pos = obstacles[idx - 1]

                # remove gap ending at x
                self.update(1,0,self.MAXX,x,0)

                if idx + 1 < len(obstacles):
                    right_pos = obstacles[idx + 1]
                    # merge gaps
                    self.update(1,0,self.MAXX,right_pos,right_pos - left_pos)

                obstacles.remove(x)

        return ans[::-1]
        

class Solution {
    struct TrieNode {
        int children[26];
        int bestLen;
        int bestIdx;
        
        TrieNode() {
            fill(begin(children), end(children), -1);
            bestLen = 1e9;
            bestIdx = 1e9;
        }
    };

public:
    vector<int> stringIndices(vector<string>& wordsContainer, vector<string>& wordsQuery) {
        vector<TrieNode> trie;
        trie.emplace_back();
        
        for (int i = 0; i < wordsContainer.size(); i++) {
            int len = wordsContainer[i].length();
            int curr = 0;
            
            if (len < trie[curr].bestLen || (len == trie[curr].bestLen && i < trie[curr].bestIdx)) {
                trie[curr].bestLen = len;
                trie[curr].bestIdx = i;
            }
            
            for (int j = len - 1; j >= 0; j--) {
                int charIdx = wordsContainer[i][j] - 'a';
                
                if (trie[curr].children[charIdx] == -1) {
                    trie[curr].children[charIdx] = trie.size();
                    trie.emplace_back();
                }
                
                curr = trie[curr].children[charIdx];
                
                if (len < trie[curr].bestLen || (len == trie[curr].bestLen && i < trie[curr].bestIdx)) {
                    trie[curr].bestLen = len;
                    trie[curr].bestIdx = i;
                }
            }
        }
        
        vector<int> ans;
        ans.reserve(wordsQuery.size());
        
        for (const string& query : wordsQuery) {
            int curr = 0;
            int len = query.length();
            
            for (int j = len - 1; j >= 0; j--) {
                int charIdx = query[j] - 'a';
                if (trie[curr].children[charIdx] == -1) {
                    break;
                }
                curr = trie[curr].children[charIdx];
            }
            ans.push_back(trie[curr].bestIdx);
        }
        
        return ans;
    }
}; 

class Solution {
  public:
  void dfs(Node* root,int key,map<int,int> &mp){
      if(!root)return ;
      mp[key]+=root->data;
      dfs(root->left,key-1,mp);
      dfs(root->right,key+1,mp);
  }
    vector<int> verticalSum(Node* root) {
        // code here
        vector<int> ans;
        map<int,int> mp;
        dfs(root,0,mp);
        for(auto i:mp){
            ans.push_back(i.second);
        }
        return ans;
    }
};
 

..... see less

0

Reply
User
Nitin Bhattar
1 hour agoMay 28, 2026 19:51 (GMT +5:30)

Easiest So

class TrieNode:
    __slots__ = ['children', 'bestLen', 'bestIdx']
    
    def __init__(self):
        self.children = {}
        self.bestLen = float('inf')
        self.bestIdx = float('inf')

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        
        for i, word in enumerate(wordsContainer):
            n = len(word)
            curr = root
            
            if n < curr.bestLen or (n == curr.bestLen and i < curr.bestIdx):
                curr.bestLen = n
                curr.bestIdx = i
                
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                
                curr = curr.children[char]
                
                if n < curr.bestLen or (n == curr.bestLen and i < curr.bestIdx):
                    curr.bestLen = n
                    curr.bestIdx = i
                    
        ans = []
        
        for query in wordsQuery:
            curr = root
            
            for char in reversed(query):
                if char not in curr.children:
                    break
                curr = curr.children[char]
            
            ans.append(curr.bestIdx)
            
        return ans

class Solution:
    def canReach(self, s: str, minJ: int, maxJ: int) -> bool:
        n = len(s)

        if int(s[-1]): return False

        dp = [False] * n
        dp[0] = True
        reach, maxR = 0, maxJ

        for i in range(minJ, n):
            if i > maxR: return False

            reach += dp[i - minJ]

            if i > maxJ:
                reach -= dp[i - maxJ - 1]

            if reach and not int(s[i]):
                dp[i] = True
                maxR = i + maxJ

        return reach > 0https://github.com/ctcrahul
        

class Solution:
    def canReach(self, s: str, minJ: int, maxJ: int) -> bool:
        n = len(s)

        if int(s[-1]): return False

        dp = [False] * n
        dp[0] = True
        reach, maxR = 0, maxJ

        for i in range(minJ, n):
            if i > maxR: return False

            reach += dp[i - minJ]

            if i > maxJ:
                reach -= dp[i - maxJ - 1]

            if reach and not int(s[i]):
                dp[i] = True
                maxR = i + maxJ

        return reach > 0

class Solution {
public:
    bool canReach(string s, int minJ, int maxJ) {
        int n = s.length();

        if (s.back() & 1) return false;

        s[0] = 'v';
        int reach = 0, maxR = maxJ;

        for (int i = minJ; i < n; i++) {
            if (i > maxR) return false;

            reach += s[i - minJ] == 'v';
            reach -= (i > maxJ) && s[i - maxJ - 1] == 'v';

            if (reach && (~s[i] & 1)) {
                s[i] = 'v';
                maxR = i + maxJ;
            }
        }

        return reach;
    }
};

class Solution {
public:
    bool canReach(string s, int minJ, int maxJ) {
        int n = s.length();

        if (s.back() & 1) return false;

        s[0] = 'v';
        int reach = 0, maxR = maxJ;

        for (int i = minJ; i < n; i++) {
            if (i > maxR) return false;

            reach += s[i - minJ] == 'v';
            reach -= (i > maxJ) && s[i - maxJ - 1] == 'v';

            if (reach && (~s[i] & 1)) {
                s[i] = 'v';
                maxR = i + maxJ;
            }
        }

        return reach;
    }
};


const canReach = (s, min, max, n = s.length) => {
    if (s.at(-1) & 1) return false;

    const dp = Array(n).fill(false);
    dp[0] = true;
    let reach = 0;
    let maxR = max;

    for (let i = min; i < n; i++) {
        if (i > maxR) return false;

        reach += dp[i - min];
        reach -= (i > max) && dp[i - max - 1];

        if (reach && !(s[i] & 1)) {
            dp[i] = true;
            maxR = i + max;
        }
    }

    return reach;
};

class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        n = len(arr)
        dp = [-1] * n

        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            best = 1

            # Right scan
            for nxt in range(i + 1, min(n, i + d + 1)):
                if arr[nxt] >= arr[i]:
                    break

                best = max(best, 1 + dfs(nxt))

            # Left scan
            for nxt in range(i - 1, max(-1, i - d - 1), -1):
                if arr[nxt] >= arr[i]:
                    break

                best = max(best, 1 + dfs(nxt))

            dp[i] = best
            return dp[i]

        return max(dfs(i) for i in range(n))

class Solution {
public:

int coin(vector<int> &arr) {
    int i = 0;
    int j = arr.size() - 1;
    
    while(i < j) {
        if(arr[i] >= arr[j]) {
            i++;
        }
        else {
            j--;
        }
    }
    
    return arr[i];
}

};


struct Edge{
    int to, nxt=-1;
};

constexpr int V=1000;
constexpr int E=V*2;

Edge POOL[E];
int idx=0;

int adj[V], deg[V];
int dp[V];

int q[V];// for queue holding idx
int front, back;

inline void addEdge(int u, int v){
    POOL[idx]={v, adj[u]};
    adj[u]=idx++;
    deg[v]++;
}
int Stack[V], top=-1;

class Solution {
public:
    static int maxJumps(vector<int>& arr, int d) {
        const int n=arr.size();
        // reset
        idx=0;
        memset(adj, -1, n*sizeof(int));
        memset(deg, 0, n*sizeof(int));
        fill(dp, dp+n, 1);
        // montonone stack
        top=-1;// clear stack
        for(int i=0; i<n; i++){
            const int x=arr[i];
            while(top>-1 && arr[Stack[top]]<x){
                int j=Stack[top--];
                if (i-j<=d) addEdge(j, i);
            }
            Stack[++top]=i;
        }
        top=-1;// clear Stack
        for(int i=n-1; i>=0; i--){
            const int x=arr[i];
            while(top>-1 && arr[Stack[top]]<x){
                int j=Stack[top--];
                if (j-i<=d) addEdge(j, i);
            }
            Stack[++top]=i;
        }

        front=back= 0;// reset for q
        for(int i=0; i<n; i++)// Push i to q if deg[i]=0
            if(deg[i]==0)
                q[back++]=i;

        while(front<back){
            int u=q[front++];
            for(int e=adj[u]; e!=-1; e=POOL[e].nxt){
                int v=POOL[e].to;
                dp[v]=max(dp[v], dp[u]+1);
                if(--deg[v]==0)
                    q[back++]=v;
            }
        }

        return *max_element(dp, dp+n);
    }
};

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int lo = 0, hi = n - 1;

        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] > nums.back()) lo = mid + 1;
            else hi = mid;
        }

        int rot = lo;
        lo = 0, hi = n - 1;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int real = (mid + rot) % n;

            if (nums[real] == target)
                return real;

            if (nums[real] < target) lo = mid + 1;
            else hi = mid - 1;
        }

        return -1;
    }
};


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        rot = bisect_left(nums, True, key=lambda n: n <= nums[-1])
        
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            real = (mid + rot) % n

            if nums[real] == target:
                return real
                
            if nums[real] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1


const search = (nums, target) => {
    let n = nums.length;
    let rot = _.sortedIndexBy(nums, nums.at(-1), c => c <= nums.at(-1));
    let lo = 0, hi = n - 1;

    while (lo <= hi) {
        let mid = (lo + hi) >> 1;
        let real = (mid + rot) % n;

        if (nums[real] === target)
            return real;

        if (nums[real] < target) lo = mid + 1;
        else hi = mid - 1;
    }

    return -1;
};

Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1


class Solution {
  public:
    void replaceElements(vector<int>& arr) {
        // code here
        int n = (int)arr.size();
        
        arr[0] = arr[0] ^ arr[1];
        int s = 0 ;
        s = s ^ arr[0];
        for(int i = 1;(i+1)<n;i++)
        {
            arr[i] = (arr[i] ^ s ^ arr[i+1]);
            s^=arr[i];
        }
        
        arr[n-1] = s ;
        
        
    }
};


class Solution {
public:

    vector<int> seg;
    const int MAXX = 50000;

    void update(int node, int l, int r, int idx, int val) {
        if (l == r) {
            seg[node] = val;
            return;
        }

        int mid = (l + r) / 2;

        if (idx <= mid)
            update(2 * node, l, mid, idx, val);
        else
            update(2 * node + 1, mid + 1, r, idx, val);

        seg[node] = max(seg[2 * node], seg[2 * node + 1]);
    }

    int query(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l)
            return 0;

        if (ql <= l && r <= qr)
            return seg[node];

        int mid = (l + r) / 2;

        return max(
            query(2 * node, l, mid, ql, qr),
            query(2 * node + 1, mid + 1, r, ql, qr)
        );
    }

    vector<bool> getResults(vector<vector<int>>& queries) {

        seg.resize(4 * (MAXX + 1), 0);

        set<int> obstacles;
        obstacles.insert(0);

        // Build final obstacle configuration
        for (auto &q : queries) {
            if (q[0] == 1) obstacles.insert(q[1]);
        }

        vector<int> pos(obstacles.begin(), obstacles.end());
        // at pos[i] we have a gap of (pos[i] - pos[i - 1]) which we are storing
        // in the segment tree
        for (int i = 1; i < (int)pos.size(); i++) {
            update(1,0,MAXX,pos[i],pos[i] - pos[i - 1]);
        }

        vector<bool> ans;

        for (int i = (int)queries.size() - 1; i >= 0; i--) {

            if (queries[i][0] == 2) {

                int x = queries[i][1];
                int sz = queries[i][2];
                // find a prev obstacle lesser than x, then we can fit the block
                //before prev or between prev to x
                auto it = prev(obstacles.upper_bound(x));

                int prevObstacle = *it;
                int best = query(1,0,MAXX,0,prevObstacle);

                best = max(best, x - prevObstacle);
                ans.push_back(best >= sz);
            }
            else {

                int x = queries[i][1]; // so we now remove x obstacle
                auto it = obstacles.find(x);
                int leftPos = *prev(it); //left of x

                update(1,0,MAXX,x,0); // update gap at x to 0 or remove gap ending at x

                auto rightIt = next(it);

                if (rightIt != obstacles.end()) {
                    int rightPos = *rightIt;
                    // merging the interval from leftpos to rightpos as one single gap
                    update(1,0,MAXX,rightPos,rightPos - leftPos);
                }

                obstacles.erase(it);
            }
        }

        reverse(ans.begin(), ans.end());
        return ans;
    }
};


class Solution:

    MAXX = 50000

    def __init__(self):
        self.seg = [0] * (4 * (self.MAXX + 1))

    def update(self, node, l, r, idx, val):
        if l == r:
            self.seg[node] = val
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(2 * node, l, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, val)

        self.seg[node] = max(
            self.seg[2 * node],
            self.seg[2 * node + 1]
        )

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return 0

        if ql <= l and r <= qr:
            return self.seg[node]

        mid = (l + r) // 2

        return max(
            self.query(2 * node, l, mid, ql, qr),
            self.query(2 * node + 1, mid + 1, r, ql, qr)
        )

    def getResults(self, queries: List[List[int]]) -> List[bool]:
        
        obstacles = SortedSet([0])

        # Build final obstacle configuration
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        pos = list(obstacles)

        # gap[pos[i]] = pos[i] - pos[i-1]
        for i in range(1, len(pos)):
            self.update(1,0,self.MAXX,pos[i],pos[i] - pos[i - 1])

        ans = []

        for i in range(len(queries) - 1, -1, -1):

            if queries[i][0] == 2:

                x = queries[i][1]
                sz = queries[i][2]

                idx = obstacles.bisect_right(x) - 1
                prev_obstacle = obstacles[idx]

                best = self.query(1,0,self.MAXX,0,prev_obstacle)
                best = max(best, x - prev_obstacle)

                ans.append(best >= sz)

            else:

                x = queries[i][1]

                idx = obstacles.index(x)
                left_pos = obstacles[idx - 1]

                # remove gap ending at x
                self.update(1,0,self.MAXX,x,0)

                if idx + 1 < len(obstacles):
                    right_pos = obstacles[idx + 1]
                    # merge gaps
                    self.update(1,0,self.MAXX,right_pos,right_pos - left_pos)

                obstacles.remove(x)

        return ans[::-1]
        

class Solution {
    struct TrieNode {
        int children[26];
        int bestLen;
        int bestIdx;
        
        TrieNode() {
            fill(begin(children), end(children), -1);
            bestLen = 1e9;
            bestIdx = 1e9;
        }
    };

public:
    vector<int> stringIndices(vector<string>& wordsContainer, vector<string>& wordsQuery) {
        vector<TrieNode> trie;
        trie.emplace_back();
        
        for (int i = 0; i < wordsContainer.size(); i++) {
            int len = wordsContainer[i].length();
            int curr = 0;
            
            if (len < trie[curr].bestLen || (len == trie[curr].bestLen && i < trie[curr].bestIdx)) {
                trie[curr].bestLen = len;
                trie[curr].bestIdx = i;
            }
            
            for (int j = len - 1; j >= 0; j--) {
                int charIdx = wordsContainer[i][j] - 'a';
                
                if (trie[curr].children[charIdx] == -1) {
                    trie[curr].children[charIdx] = trie.size();
                    trie.emplace_back();
                }
                
                curr = trie[curr].children[charIdx];
                
                if (len < trie[curr].bestLen || (len == trie[curr].bestLen && i < trie[curr].bestIdx)) {
                    trie[curr].bestLen = len;
                    trie[curr].bestIdx = i;
                }
            }
        }
        
        vector<int> ans;
        ans.reserve(wordsQuery.size());
        
        for (const string& query : wordsQuery) {
            int curr = 0;
            int len = query.length();
            
            for (int j = len - 1; j >= 0; j--) {
                int charIdx = query[j] - 'a';
                if (trie[curr].children[charIdx] == -1) {
                    break;
                }
                curr = trie[curr].children[charIdx];
            }
            ans.push_back(trie[curr].bestIdx);
        }
        
        return ans;
    }
}; 

class Solution {
  public:
  void dfs(Node* root,int key,map<int,int> &mp){
      if(!root)return ;
      mp[key]+=root->data;
      dfs(root->left,key-1,mp);
      dfs(root->right,key+1,mp);
  }
    vector<int> verticalSum(Node* root) {
        // code here
        vector<int> ans;
        map<int,int> mp;
        dfs(root,0,mp);
        for(auto i:mp){
            ans.push_back(i.second);
        }
        return ans;
    }
};
 

..... see less

0

Reply
User
Nitin Bhattar
1 hour agoMay 28, 2026 19:51 (GMT +5:30)

Easiest So

class TrieNode:
    __slots__ = ['children', 'bestLen', 'bestIdx']
    
    def __init__(self):
        self.children = {}
        self.bestLen = float('inf')
        self.bestIdx = float('inf')

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        
        for i, word in enumerate(wordsContainer):
            n = len(word)
            curr = root
            
            if n < curr.bestLen or (n == curr.bestLen and i < curr.bestIdx):
                curr.bestLen = n
                curr.bestIdx = i
                
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                
                curr = curr.children[char]
                
                if n < curr.bestLen or (n == curr.bestLen and i < curr.bestIdx):
                    curr.bestLen = n
                    curr.bestIdx = i
                    
        ans = []
        
        for query in wordsQuery:
            curr = root
            
            for char in reversed(query):
                if char not in curr.children:
                    break
                curr = curr.children[char]
            
            ans.append(curr.bestIdx)
            
        return ans

class Solution:
    def canReach(self, s: str, minJ: int, maxJ: int) -> bool:
        n = len(s)

        if int(s[-1]): return False

        dp = [False] * n
        dp[0] = True
        reach, maxR = 0, maxJ

        for i in range(minJ, n):
            if i > maxR: return False

            reach += dp[i - minJ]

            if i > maxJ:
                reach -= dp[i - maxJ - 1]

            if reach and not int(s[i]):
                dp[i] = True
                maxR = i + maxJ

        return reach > 0https://github.com/ctcrahul
        

class Solution:
    def canReach(self, s: str, minJ: int, maxJ: int) -> bool:
        n = len(s)

        if int(s[-1]): return False

        dp = [False] * n
        dp[0] = True
        reach, maxR = 0, maxJ

        for i in range(minJ, n):
            if i > maxR: return False

            reach += dp[i - minJ]

            if i > maxJ:
                reach -= dp[i - maxJ - 1]

            if reach and not int(s[i]):
                dp[i] = True
                maxR = i + maxJ

        return reach > 0

class Solution {
public:
    bool canReach(string s, int minJ, int maxJ) {
        int n = s.length();

        if (s.back() & 1) return false;

        s[0] = 'v';
        int reach = 0, maxR = maxJ;

        for (int i = minJ; i < n; i++) {
            if (i > maxR) return false;

            reach += s[i - minJ] == 'v';
            reach -= (i > maxJ) && s[i - maxJ - 1] == 'v';

            if (reach && (~s[i] & 1)) {
                s[i] = 'v';
                maxR = i + maxJ;
            }
        }

        return reach;
    }
};

class Solution {
public:
    bool canReach(string s, int minJ, int maxJ) {
        int n = s.length();

        if (s.back() & 1) return false;

        s[0] = 'v';
        int reach = 0, maxR = maxJ;

        for (int i = minJ; i < n; i++) {
            if (i > maxR) return false;

            reach += s[i - minJ] == 'v';
            reach -= (i > maxJ) && s[i - maxJ - 1] == 'v';

            if (reach && (~s[i] & 1)) {
                s[i] = 'v';
                maxR = i + maxJ;
            }
        }

        return reach;
    }
};


const canReach = (s, min, max, n = s.length) => {
    if (s.at(-1) & 1) return false;

    const dp = Array(n).fill(false);
    dp[0] = true;
    let reach = 0;
    let maxR = max;

    for (let i = min; i < n; i++) {
        if (i > maxR) return false;

        reach += dp[i - min];
        reach -= (i > max) && dp[i - max - 1];

        if (reach && !(s[i] & 1)) {
            dp[i] = true;
            maxR = i + max;
        }
    }

    return reach;
};

class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        n = len(arr)
        dp = [-1] * n

        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            best = 1

            # Right scan
            for nxt in range(i + 1, min(n, i + d + 1)):
                if arr[nxt] >= arr[i]:
                    break

                best = max(best, 1 + dfs(nxt))

            # Left scan
            for nxt in range(i - 1, max(-1, i - d - 1), -1):
                if arr[nxt] >= arr[i]:
                    break

                best = max(best, 1 + dfs(nxt))

            dp[i] = best
            return dp[i]

        return max(dfs(i) for i in range(n))

class Solution {
public:

int coin(vector<int> &arr) {
    int i = 0;
    int j = arr.size() - 1;
    
    while(i < j) {
        if(arr[i] >= arr[j]) {
            i++;
        }
        else {
            j--;
        }
    }
    
    return arr[i];
}

};


struct Edge{
    int to, nxt=-1;
};

constexpr int V=1000;
constexpr int E=V*2;

Edge POOL[E];
int idx=0;

int adj[V], deg[V];
int dp[V];

int q[V];// for queue holding idx
int front, back;

inline void addEdge(int u, int v){
    POOL[idx]={v, adj[u]};
    adj[u]=idx++;
    deg[v]++;
}
int Stack[V], top=-1;

class Solution {
public:
    static int maxJumps(vector<int>& arr, int d) {
        const int n=arr.size();
        // reset
        idx=0;
        memset(adj, -1, n*sizeof(int));
        memset(deg, 0, n*sizeof(int));
        fill(dp, dp+n, 1);
        // montonone stack
        top=-1;// clear stack
        for(int i=0; i<n; i++){
            const int x=arr[i];
            while(top>-1 && arr[Stack[top]]<x){
                int j=Stack[top--];
                if (i-j<=d) addEdge(j, i);
            }
            Stack[++top]=i;
        }
        top=-1;// clear Stack
        for(int i=n-1; i>=0; i--){
            const int x=arr[i];
            while(top>-1 && arr[Stack[top]]<x){
                int j=Stack[top--];
                if (j-i<=d) addEdge(j, i);
            }
            Stack[++top]=i;
        }

        front=back= 0;// reset for q
        for(int i=0; i<n; i++)// Push i to q if deg[i]=0
            if(deg[i]==0)
                q[back++]=i;

        while(front<back){
            int u=q[front++];
            for(int e=adj[u]; e!=-1; e=POOL[e].nxt){
                int v=POOL[e].to;
                dp[v]=max(dp[v], dp[u]+1);
                if(--deg[v]==0)
                    q[back++]=v;
            }
        }

        return *max_element(dp, dp+n);
    }
};

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int lo = 0, hi = n - 1;

        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] > nums.back()) lo = mid + 1;
            else hi = mid;
        }

        int rot = lo;
        lo = 0, hi = n - 1;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int real = (mid + rot) % n;

            if (nums[real] == target)
                return real;

            if (nums[real] < target) lo = mid + 1;
            else hi = mid - 1;
        }

        return -1;
    }
};


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        rot = bisect_left(nums, True, key=lambda n: n <= nums[-1])
        
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            real = (mid + rot) % n

            if nums[real] == target:
                return real
                
            if nums[real] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1


const search = (nums, target) => {
    let n = nums.length;
    let rot = _.sortedIndexBy(nums, nums.at(-1), c => c <= nums.at(-1));
    let lo = 0, hi = n - 1;

    while (lo <= hi) {
        let mid = (lo + hi) >> 1;
        let real = (mid + rot) % n;

        if (nums[real] === target)
            return real;

        if (nums[real] < target) lo = mid + 1;
        else hi = mid - 1;
    }

    return -1;
};

Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
