class Solution {
    public int characterReplacement(String s, int k) {
        int maxFreq=0;
        int left=0;
        int maxLength=0;
        int[] freq=new int[26];
        for(int i=0;i<s.length();i++){
            int a=s.charAt(i)-'A';
         freq[a]++;
        maxFreq=Math.max(maxFreq,freq[a]);
        int replace=(i-left+1)-maxFreq;
        while(replace>k){
            int leftindex=s.charAt(left)-'A';
            freq[leftindex]--;
            left++;
            replace=(i-left+1)-maxFreq;
          }
        maxLength=Math.max(maxLength,i-left+1);
        }
        return maxLength;
    }
}