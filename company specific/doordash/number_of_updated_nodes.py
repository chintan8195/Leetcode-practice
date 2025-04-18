""" 
At DoorDash, menus are updated daily even hourly to keep them up-to-date. Each menu can be regarded as a tree. A menu can have many categories; each category can have many menu_items; each menu_item can have many item_extras; An item_extra can have many item_extra_options...

class Node {
        String key;
        int value;
        boolean active;
        List<Node> children;
 }
We will compare the new menu sent from the merchant with our existing menu. Each item can be considered as a node in the tree. The definition of a node is defined above. Either value change or the active status change means the node has been changed. There are times when the new menu tree structure is different from existing trees, which means some nodes are set to null. In this case, we only do soft delete for any nodes in the menu. If that node or its sub-children are null, we will treat them ALL as inactive. There are no duplicate nodes with the same key.

Return the number of changed nodes in the tree.

        Existing tree                                        
         a(1, T)                                                
        /       \                                                          
     b(2, T)   c(3, T)                                               
    /     \           \                                                        
d(4, T) e(5, T)   f(6, T)                                               

        New tree 
        a(1, T)
            \
           c(3, F)
               \
               f(66, T)
a(1, T) a is the key, 1 is the value, T is True for active status For example, there are a total of 5 changed nodes. Node b, Node d, Node e are automatically set to inactive. The active status of Node c and the value of Node f changed as well.

      Existing tree                                                   
        a(1, T)                                                 
      /         \                                                 
    b(2, T)   c(3, T)                                   
  /       \           \                                          
d(4, T) e(5, T)      g(7, T)                       

            New tree
            a(1, T)
          /        \                                             
   b(2, T)         c(3, T)  
   /    |    \           \    
d(4, T) e(5, T) f(6, T)    g(7, F) 

"""