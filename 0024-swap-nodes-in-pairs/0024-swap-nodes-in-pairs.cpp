/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(!head || !(head->next)) return head;
        ListNode* prev=head;
        ListNode* curr=head->next;
        head=curr;
        while(curr) {
            ListNode* nextptr=curr->next;
            curr->next=prev;
            if(nextptr && nextptr->next==NULL) prev->next=nextptr; // odd number of nodes
            else if(nextptr && prev) prev->next=nextptr->next; // even number of nodes
            else if(prev->next==curr) prev->next=NULL; // end of linked list
            prev=nextptr;
            if(nextptr) curr=nextptr->next;
            else curr=NULL;
        }
        return head;
    }
};