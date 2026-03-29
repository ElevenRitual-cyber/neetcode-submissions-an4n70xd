class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer,Integer> hash= new HashMap<>();
        for(int i:nums){
            if(hash.containsKey(i)){
                return true;
            }else{
                hash.put(i,hash.getOrDefault(i,0)+1);
            }
        }
        return false;

 
    }
}
