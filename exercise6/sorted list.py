#LISTNODE METHOD
class ListNode(object):
    #LISTNODE is a linked list node and not a python list, we cannot directly iterate over ListNode like with python lists
    #listnode is usually part of a linked list where each node contains a valueand a next pointer to the next node.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
   #__repr__ method is used to ensure that when listnode is printed it will print the values and not the memor address
    def __repr__(self):
        return str(self.val)
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # create a dummy node to build the merged list or to append nodes to it without worrying whether the merged list is empty
        #dummy=ListNode() a dummy node is created with a intial valye of 0. This node does not contain meaningful data it serves as a starting point for building the merged list
        #current=dummy the current value is initialized to point the dummy node. As we append new nodes to the merged list, current will move forward
        dummy = ListNode()
        current = dummy
        #traversing and merging: the loop processes each value on list1 and list2 one at a time and compare the values, and append smaller one to the merged list (current)
        while list1 and list2: #while there are values in both list 1 and list 2
            if list1.val <= list2.val: #if 1st value in list 1 is less than or equal to 1st value in list 2,
                current.next = list1 #we append the current value in list 1 to the merged list (current) that we initialized through dummy
                list1 = list1.next # now we take the next value in the list1 and iteratethe loop
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            print(current)
        if list1: #if list1 or list2 still has values just add them to the merged list
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next #return the merged list which starts from dummy.next

def create_linked_list(lst): #this function will create a linked list from user input to be passed into the merge two list function
    dummy = ListNode() #lets say the list from user is [1,2,3]
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next #BEFORE RETURNING: dummy -> 1 -> 2 -> 3 -> none | AFTER RETURNING: 1 -> 2 -> 3 -> None. Convertes a pythong list into linked list

# Helper function to print the contents of the linked list
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

vars1 = input("Enter list1: ").split(",")
vars2 = input("Enter list2: ").split(",")

listx = [int(i) for i in vars1]
listy = [int(i) for i in vars2]

list1 = create_linked_list(listx)
list2 = create_linked_list(listy)

solution = Solution()
output = solution.mergeTwoLists(list1, list2)
print(output)
print_linked_list(output)




#METHOD 2 WITHOUT USING LINKED LIST
# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         value1 = list1
#         value2 = list2
#         empty_list = []
#         for x in value1:
#             empty_list.append(x)
#         print(empty_list)
#
#         for y in value2:
#             #find the correct index position to insert y in empty list
#             for z in range(len(empty_list)):
#                 if y <= empty_list[z]:
#                     empty_list.insert(z, y)
#                     break
#             else:
#                 empty_list.append(y)
#         return empty_list
# solution = Solution()
# vars1 = input("Enter list1: ").split(",")
# vars2 = input("Enter list2: ").split(",")
#
# list1 = [int(i) for i in vars1]
# list2 = [int(i) for i in vars2]
# print(list1)
# print(list2)
# output = solution.mergeTwoLists(list1=list1, list2=list2)
# print(output)


#[1,2,4] [1,3,4] empty_list=[1,2,3] => for z in range [0,2]
#loop1 if 1 <= empty_list[0] => 1 <= 1 yes so empty_list.insert(0, 1) insert in position 0 number 1 => empty_list = [1,1,2,3,4]
#loop2 if 3 <= empty_list[0/1] => 3 <= 1 no -> 3<= empty_list[2] => 3<=2 no => 3<=empty_list[3] => 3<= 4 yes so empty_list.insert(3, 3) insert in position 4 number 3 list looks like [1,1,2,3,4]
#loop3 if 4 <= empty_list[0/1] => 4 <= 1 no -> 4<= empty_list[2] => 4<=2 no => 4<=empty_list[3] => 4<= 3 no 4<=empty_list[4] yes so empty_list.insert(4, 4) insert in position 4 number 4 list looks like [1,1,2,3,4,4]
