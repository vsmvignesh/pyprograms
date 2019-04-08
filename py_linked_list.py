#!/usr/bin/python

import sys
import copy

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def addAtBeginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
            
            
    def addAtLast(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        lastnode = self.head
        while lastnode.next:
            lastnode = lastnode.next
        lastnode.next = new_node
        

    def printList(self):
        current_node = self.head
        if not current_node:
            print("The List is empty. Add some entries and try to print again.")
            return
        print("\n")
        while current_node is not None:
            print current_node.data
            current_node = current_node.next
        print("\n")   
        
    def printReverse(self):
        
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node    
        

            
            
            
def main():
    l_list = LinkedList()
    added = 0
    num = int(input("\nEnter the number of entries to add: "))
    while True:
        choice = int(input("\n1. Add at Beginning\n2. Add at the End\n3. Print the List\n4. Print List in Reverse\n5. Exit\n\nEnter Choice: "))
        if choice not in [1, 2, 3, 4,5]:
            sys.exit("Invalid Option. Try again Later...")
        if choice == 3:
            l_list.printList()
        elif choice == 5:
            print("Exiting.. Thank You!")
            return 0
        elif choice == 4:
            r_list = copy.deepcopy(l_list)
            r_list.printReverse()
            print("The reversed list is: ")
            r_list.printList()
            del r_list
        else:
            if added < num:
                node_data = raw_input("\nEnter the input data: ")
                added += 1
                if choice == 1:
                    l_list.addAtBeginning(node_data)
                elif choice == 2:
                    l_list.addAtLast(node_data)
            else:
                print("Finished adding '{0}' entries.".format(num))
                l_choice = int(input("Enter 1 to add more entries or 99 to go back: "))
                if l_choice not in [1, 99]:
                    sys.exit("Invalide Option... Try again later!!")
                else:
                    if l_choice == 1:
                        new_num = int(input("Enter the number of entries you want to add more than '{0}': ".format(num)))
                        num += new_num
                    elif l_choice == 99:
                        break
                        
            
            
            
            
if __name__ == "__main__":
    main()            
