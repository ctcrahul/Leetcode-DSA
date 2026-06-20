AI
⬇️
Machine Learning
⬇️
Deep Learning
⬇️
Generative AI
⬇️
LLMs

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
