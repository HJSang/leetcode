/* 141. Linked List Cycle
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, 
we use an integer pos which represents the position 
(0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

*/

/* Solution: traversal with one step and two steps.
If there exists a loop, they will meet.

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
    bool hasCycle(ListNode *head) {
        // 1 node
        if(head == NULL || head->next == NULL) return false;
        // init
        ListNode* slow = head;
        ListNode* fast = head->next;
        while(slow != fast){
            // break condition
            if(fast->next == NULL || fast->next->next == NULL) return false;
            slow = slow->next;
            fast = fast->next->next;
        }
        return true;
    }
}; 