
A binary tree doesn't have a particular sort order
```
            2
          /   \
        10     3
      /   \   /  \
     9    8  6    4 
                   \ 
                    5
```
A binary search tree has a particular sort order.     
All values on left must be smaller than parent.      
All values on right must be more than parent.
```
            6                1st depth
          /    \
        4         8          2nd depth
      /   \      /   \
     3     5    7     10     3rd depth
    /  \   /\  / \    / \ 
   n   n  n  n n  n  n    9  4th depth
```
#### Binary Search Tree vs Array
Adding to a sorted array is 0(n) time. ```[1,2,3,5,6]```     
Adding to a bineary search tree is log(n) time.       
In some situations you get an 0(n) search in a BST.  As in the below example.     
This would be inbalanced.            
``` 
            1
             \
              2
               \
                3
                 \
                  4
```