class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
      //1.1 create a string hashmap to see if there is an anagram
      //1.2 put all the strings in the hashmap
      //1.3 if string does not have same values put to an array.
      //1.4 if string has same value append it to array and look for more

    HashMap<String, List<String>> group = new HashMap<>();
    for (String s : strs) {
        int [] count = new int[26];
        for (char c : s.toCharArray()){
            count[c - 'a']++;
        }
        String key = Arrays.toString(count);
        group.putIfAbsent(key, new ArrayList<>());
        group.get(key).add(s);
    }

    return new ArrayList<>(group.values());

    }
}
