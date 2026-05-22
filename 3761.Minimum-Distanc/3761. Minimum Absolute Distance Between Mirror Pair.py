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
