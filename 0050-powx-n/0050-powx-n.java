class Solution {
    public double myPow(double x, int n) {
        
         if(n==0) return 1;
        else if(x>0){
          double result = Math.pow(x,n);
          return result;
        }
        else if(x<0){
            double result1 = Math.pow(x,n);
            return result1;
        }
        return 0;
    }
}