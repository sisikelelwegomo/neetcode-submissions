class Solution {
    public int[] twoSum(int[] nums, int target) {
       HashMap<Integer, Integer> indices = new HashMap<Integer, Integer>();

       for(int i = 0; i < nums.length; i++){
        indices.put(nums[i], i);
       }

       for(int i = 0; i < nums.length; i++){
       int differ = target - nums[i];

        if (indices.containsKey(differ) && indices.get(differ) !=i){
            return new int[]{i, indices.get(differ)};
        }
       }

       return new int[0];

    }
}
