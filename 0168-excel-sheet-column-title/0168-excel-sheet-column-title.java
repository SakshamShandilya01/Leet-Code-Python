class Solution {
    public String convertToTitle(int columnNumber) {
        String s = "";
        while(columnNumber>0){
            columnNumber--;
            s=(char)('A'+ (columnNumber%26))+s;
            columnNumber/=26;
        }
        return s;
    }
}