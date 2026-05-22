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
