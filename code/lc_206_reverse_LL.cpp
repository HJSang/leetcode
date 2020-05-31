/* 206. Reverse Linked List
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively.
 Could you implement both?
*/

//iterative way
// a->b->c
// a<- b <- c == c->b->a
//
class Solution {
public:
	ListNode* reverseList(ListNode* head)
	{
		ListNode* pre(NULL), *cur(head), *next;
		while(cur)
		{
			next = cur->next;
			cur->next = pre;
			pre = cur;
			cur = next;
		}
		return pre;
	}
};

//Recursive solution
//
 class Solution {
 public:
 	ListNode* reverseList(ListNode* head)
 	{
 		if(!head || !head->next) return head;
 		ListNode* node = reverseList(head->next);
 		head->next->next = head;
 		head->next = NULL;
 		return node;
 	}
 };