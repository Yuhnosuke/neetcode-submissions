class Solution {

    List<List<Integer>> res;

    public List<List<Integer>> combinationSum(int[] nums, int target) {
        res = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();
        backtrack(0, curr, 0, target, nums);
        return res;
    }

    public void backtrack(int i, List<Integer> curr, int curr_sum, int target, int[] nums) {
        if (curr_sum > target || i >= nums.length) {
            return;
        }

        if (curr_sum == target) {
            res.add(new ArrayList<>(curr));
            return;
        }

        curr.add(nums[i]);
        backtrack(i, curr, curr_sum + nums[i], target, nums);

        curr.remove(curr.size() - 1);
        backtrack(i + 1, curr, curr_sum, target, nums);
    }
}
