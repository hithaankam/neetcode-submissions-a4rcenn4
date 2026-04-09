class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> triplets = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            for (int j = i + 1; j < nums.length - 1; j++) {
                for (int k = j + 1; k < nums.length; k++) {
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        List<Integer> triplet = new ArrayList<>();
                        triplet.add(nums[i]);
                        triplet.add(nums[j]);
                        triplet.add(nums[k]);
                        Collections.sort(triplet);
                        if (!checkTriplet(triplets, triplet)) {
                            triplets.add(triplet);
                        }
                    }
                }
            }
        }

        return triplets;
    }

    public static boolean checkTriplet(List<List<Integer>> triplets, List<Integer> triplet) {
        for (List<Integer> existingTriplet : triplets) {
            if (existingTriplet.equals(triplet)) {
                return true; 
            }
        }
        return false;
    }
}
