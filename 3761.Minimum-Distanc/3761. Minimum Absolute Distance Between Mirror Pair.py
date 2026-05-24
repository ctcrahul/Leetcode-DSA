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
