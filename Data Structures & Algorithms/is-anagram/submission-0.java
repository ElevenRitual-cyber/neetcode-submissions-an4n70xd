class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character,Integer> map= new HashMap<>();
        for(char ch:s.toCharArray()){
           map.put(ch,map.getOrDefault(ch,0)+1);
        }
        System.out.println(map);
        for(char ch:t.toCharArray()){
            if(map.containsKey(ch)){
                 map.put(ch,map.get(ch)-1);
            }else{
                return false;
            }
        }
        System.out.println(map);
        boolean result= map.values().stream().anyMatch(val -> val>=1);
        return !result;


    }
}
