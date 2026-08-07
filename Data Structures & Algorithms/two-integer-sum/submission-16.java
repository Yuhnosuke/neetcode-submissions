class Solution {
    public int[] twoSum(int[] nums, int target) {

        Map<Integer, Integer> numToIndex = new HashMap<>();
        for (int i = 0; i < nums.length; i ++) {
            numToIndex.put(nums[i], i);
        }

        for (int i = 0; i < nums.length; i ++) {
            int diff = target - nums[i];
            if (numToIndex.containsKey(diff) && numToIndex.get(diff) != i) {
                return new int[]{i, numToIndex.get(diff)};
            }
        }
    return new int[2];
    }
}
