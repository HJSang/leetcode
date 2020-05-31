/* 328. Odd Even Linked List
Given a singly linked list, group all odd nodes together 
followed by the even nodes. Please note here we are talking 
about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) 
space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        // special cases: 1 or 2 nodes
        if(head==NULL || head->next==NULL || head->next->next==NULL)
        {
            return head;
        }
        //init
        ListNode* odd_ptr = head;
        ListNode* even_ptr = head->next;
        //record head of even_ptr
        ListNode* head_even_ptr = even_ptr;
        while(odd_ptr->next!=NULL && even_ptr->next!=NULL)
        {
            //cout<<"odd_ptr value:\t"<<odd_ptr->val<<endl;
            odd_ptr->next = odd_ptr->next->next;
            //cout<<"odd_ptr next value:\t"<<odd_ptr->next->val<<endl;
            if(odd_ptr->next!=NULL) odd_ptr = odd_ptr->next;
            //cout<<"even_ptr value:\t"<<even_ptr->val<<endl;
            even_ptr->next=even_ptr->next->next;
            //cout<<"even_ptr next value:\t"<<even_ptr->next->val<<endl;
            if(even_ptr->next!=NULL) even_ptr = even_ptr->next;
        }
        // odd followed by even
        odd_ptr->next=head_even_ptr;
        return head;  
    }
};