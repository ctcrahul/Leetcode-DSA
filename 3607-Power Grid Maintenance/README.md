# ⚡ Power Grid Maintenance (LeetCode 3607)

## 🔗 Problem Link

👉 [Power Grid Maintenance (LeetCode 3607)](https://leetcode.com/problems/power-grid-maintenance/?utm_source=chatgpt.com)

---

## 🧠 Problem Summary

You are given:

* `c` power stations labeled from `1` to `c`
* `connections` representing bidirectional cables
* `queries` of two types:

  * `[1, x]` → Maintenance check
  * `[2, x]` → Station goes offline

### Rules:

* Stations form **connected components (power grids)**
* Initially, **all stations are online**
* If a station is offline:

  * Find the **smallest online station in the same component**
  * If none exist → return `-1`

---

## 💡 Key Insight

This is NOT a dynamic graph problem.

👉 Connectivity NEVER changes
👉 Only node status (online/offline) changes ([hellointerview.com][1])

So:

* Use **DSU (Union-Find)** to build components
* Maintain **active nodes per component**

---

## ⚙️ Approach

1. Use **Union-Find** to group stations into components
2. Maintain:

   * `online[]` → track active stations
   * component-wise structure → sorted active nodes
3. Process queries:

   * `[2, x]`: mark offline
   * `[1, x]`:

     * if online → return `x`
     * else → return smallest active node in component

---

## 🚀 Time Complexity

* DSU build → `O(n + c)`
* Query handling → `O(log n)` (optimized)

---

## 🧾 Python Implementation

```python
from collections import defaultdict
import bisect

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1


class Solution:
    def powerGridMaintenance(self, c, connections, queries):
        dsu = DSU(c)

        for u, v in connections:
            dsu.union(u, v)

        comp = defaultdict(list)
        for i in range(1, c + 1):
            root = dsu.find(i)
            comp[root].append(i)

        for k in comp:
            comp[k].sort()

        online = [True] * (c + 1)
        res = []

        for t, x in queries:
            root = dsu.find(x)

            if t == 1:
                if online[x]:
                    res.append(x)
                else:
                    found = -1
                    for node in comp[root]:
                        if online[node]:
                            found = node
                            break
                    res.append(found)
            else:
                online[x] = False

        return res
```

---

## ⚠️ Brutal Reality

Your current approach = **semi-correct but weak at scale**

Problem:

* You scan full components → worst case **O(n) per query**

Better:

* Use **SortedSet / Heap / TreeSet**
* Maintain minimum dynamically → `O(log n)`

---

## 🎯 What You Should Fix (No Excuses)

1. Replace list with:

   * `SortedList` (Python)
2. Maintain:

   ```
   root → sorted active nodes
   ```
3. Remove node in `log n`
4. Get min instantly

---

## 🧠 Final Take

If you keep writing solutions like this:

* You’ll pass basic tests
* You’ll fail real interviews

Start thinking:

> “What happens at 200,000 queries?”

That’s the level you need to operate at.

[1]: https://www.hellointerview.com/community/questions/power-grid-maintenance/a8336ca1-fed5-4f5d-9bb7-c1fd45c36615?utm_source=chatgpt.com "Leetcode 3607. Power Grid Maintenance"
