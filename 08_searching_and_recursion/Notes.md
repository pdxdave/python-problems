A basic recursion example

```
def simpleExample(arr, item, current_index):
    
    if arr[current_index] == item:
        return current_index

    return simpleExample(arr, item, current_index + 1)


the_array = [1,2,3,4,5,6,7,8,9]
print(simpleExample(the_array, 7, 0))
# returns 6
```