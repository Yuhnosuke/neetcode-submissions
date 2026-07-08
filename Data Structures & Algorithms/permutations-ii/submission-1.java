class Solution {
    private List<List<Integer>> res;
    private Map<Integer, Integer> numToCount;

    public List<List<Integer>> permuteUnique(int[] nums) {
        res = new ArrayList<>();
        numToCount = new HashMap<>();
        List<Integer> curr = new ArrayList<>();

        for (int num : nums) {
            numToCount.put(num, numToCount.getOrDefault(num, 0) + 1);
        }

        this.backtrack(nums, curr);
        return res;
    }

    private void backtrack(int[] nums, List<Integer> curr) {
        if (curr.size() == nums.length) {
            this.res.add(new ArrayList<>(curr));
            return;
        }

        for (int num : numToCount.keySet()) {
            if (numToCount.get(num) <= 0) {
                continue;
            }

            curr.add(num);
            numToCount.put(num, numToCount.get(num) - 1);

            this.backtrack(nums, curr);

            curr.remove(curr.size() - 1);
            numToCount.put(num, numToCount.get(num) + 1);
        }
    }
}