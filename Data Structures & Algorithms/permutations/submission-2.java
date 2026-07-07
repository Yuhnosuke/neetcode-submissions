class Solution {
    
    List<List<Integer>> res;

    public List<List<Integer>> permute(int[] nums) {
        res = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();

        this.backtrack(curr, nums);
        return res;
    }

    public void backtrack(List<Integer> curr, int[] nums) {
        if (curr.size() == nums.length) {
            res.add(new ArrayList<>(curr));
            return;
        }

        for (int i = 0; i < nums.length; i ++) {
            int num = nums[i];

            if (!curr.contains(num)) {
                curr.add(num);
                this.backtrack(curr, nums);
                curr.remove(curr.size() - 1);
            }
        }
    }
}
