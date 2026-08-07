class Solution {
    

    public boolean hasDuplicate(int[] nums) {
        Set<Integer> seens = new HashSet<>();

        for (int i = 0; i < nums.length; i ++) {
            if (seens.contains(nums[i])) {
                return true;
            }
            seens.add(nums[i]);
        }
        return false;
    }
}