/* 2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order and each of their nodes contain a single digit.

Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        //initialize
        ListNode head(0);
        ListNode* node = &head;
        int next_reminder = 0;
        while(l1!=nullptr || l2!=nullptr||next_reminder)
        {
            int a= l1!=nullptr? l1->val:0;
            int b= l2!=nullptr? l2->val:0;
            ListNode* new_node = new ListNode((a + b + next_reminder) % 10);
            //link
            node->next = new_node;
            //update
            next_reminder = (a + b + next_reminder)/10;
            if(l1!=nullptr) l1=l1->next;
            if(l2!=nullptr) l2=l2->next;
            node=node->next;
        }
        return head.next;
        
    }
};