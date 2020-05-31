/* 234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?

*/

/* method 1: Use Stack
1) Traverse the given list from head to tail and push visited node to stack.
2) Traverse the list again. For every visited node, pop a node from stack
 and compare data of popped node with currently visited node.
3) if all nodes macthed, then return true, else false.
*/


/* method 2: By reversing the list 
1) Get the middle of the linked list.
  1a) Get the middle of the list. Move slow_ptr by 1 
          and fast_ptrr by 2, slow_ptr will have the middle 
          node .
2) Reverse the second half of the linked list.
  2a) fast_ptr would become NULL when there are even elements in list.  
           And not NULL for odd elements. We need to skip the middle node  
           for odd case and store it somewhere so that we can restore the 
           original list.
  2b) https://www.geeksforgeeks.org/reverse-a-linked-list/
3) chekc if the first half and the second half are identical.
4) Construct the original linked list by reversing the second 
half again and attaching it back to the first half
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
    ListNode* reverse(ListNode* head)
    {
        //init
        ListNode* prev = nullptr;
        while(head!=NULL)
        {
            ListNode* post = head->next;
            head->next = prev;
            prev = head;
            head = post;
        }
        return prev;
    }
    bool isPalindrome(ListNode* head) {
        //find the middle node
        int count =0;
        for(ListNode* node=head; node;node=node->next)
        {
            ++count;
        }
        ListNode* secondHead = head;
        for(int i=0; i<count/2; i++)
        {
            secondHead=secondHead->next;
        }
        // odd count or even count
        if(count & 1)
        {
            secondHead=secondHead->next;
        }
        //reverse
        secondHead = reverse(secondHead);
        //compare
        for(int i=0;i<count/2; i++)
        {
            if(head->val!=secondHead->val)
                return false;
            head = head->next;
            secondHead=secondHead->next;
        }
        return true;
    }
};

/* METHOD 3 (Using Recursion)
Use two pointers left and right. Move right and left using recursion and check for following in each recursive call.
1) Sub-list is palindrome.
2) Value at current left and right are matching.
*/
