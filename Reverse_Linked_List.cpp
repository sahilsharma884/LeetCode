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
    ListNode* reverseList(ListNode* head) {
        //store previous and current(i.e next node) node
        ListNode* prev = NULL;
        ListNode* curr = NULL;
        
        // if only contain one element
        if (head == NULL || head->next == NULL){
            return head;
        }
        else {
            // otherwise iterate over all the elements
            curr = head->next;
        }
        
        // iterate over prev-head-current
        while (head->next != NULL) {
            head->next = prev;
            prev = head;
            head = curr;
            curr = head->next;
        }

        // for last element
        head->next = prev;
        
        return head;
    }
};
