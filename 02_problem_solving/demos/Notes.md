#### In place
```
def triple_list_in_place(int_list):
    for i in range(len(int_list)):
        int_list[i] *= 3

    # No return b/c we've modified the original list in place.  


num_list = [1,2,3,4,5]
print(triple_list_in_place(num_list)) 
```


#### Out of place
```
def triple_list_out_of_place(int_list):
    # Allocate a new list with enough room for all the elements
    tripled_list = [None] * len(int_list)

    for i in range(len(int_list)):
        tripled_list[i] = int_list[i] * 3

    return tripled_list

num_list = [1,2,3,4,5]
print(triple_list_out_of_place(num_list))
```