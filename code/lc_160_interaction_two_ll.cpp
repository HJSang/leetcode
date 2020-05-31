/* 160. Intersection of Two Linked Lists

Write a program to find the node at which the 
intersection of two singly linked lists begins.

Notes:

If the two linked lists have no intersection at all,
 return null.
The linked lists must retain their original structure 
after the function returns.
You may assume there are no cycles anywhere in the 
entire linked structure.
Your code should preferably run in O(n) time and 
use only O(1) memory.

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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        //count lenfths for two lists
        int len1=0, len2=0;
        ListNode* nodeA = headA;
        ListNode* nodeB = headB;
        while(nodeA!=NULL)
        {
            len1++;
            nodeA=nodeA->next;
        }
        while(nodeB!=NULL)
        {
            len2++;
            nodeB=nodeB->next;
        }
        //move to the same starting point
        nodeA=headA;
        nodeB=headB;
        if(len1<len2)
        {
            for(int i=0; i<len2-len1; i++) nodeB=nodeB->next;
        }
        else
        {
            for(int i=0; i<len1-len2; i++) nodeA=nodeA->next;
        }
        //compare
        while(nodeA!=NULL)
        {
            if(nodeA==nodeB) return nodeA;
            nodeA=nodeA->next;
            nodeB=nodeB->next;
        }
        return NULL;
        
    }
};

