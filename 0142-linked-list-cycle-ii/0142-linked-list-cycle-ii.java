public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode x = head;
        ListNode y = head;
        while(y!=null && y.next!=null){
            x = x.next;
            y = y.next.next;
            if(x==y){
                x = head;
                while(x!=y){
                    x = x.next;
                    y = y.next;
                }
                return x;
            }
        }
        return null;
    }
}