class Solution {
    
    List<List<Integer>> res;

    public List<List<Integer>> subsets(int[] nums) {
        res = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();
        
        backtrack(0, curr, nums);
        return res;
    }

    public void backtrack(int i, List<Integer> curr, int[] nums) {
        if (i == nums.length) {
            res.add(new ArrayList<>(curr));
            return;
        }

        curr.add(nums[i]);
        backtrack(i + 1, curr, nums);

        curr.remove(curr.size() - 1);
        backtrack(i + 1, curr, nums);
    }
}
