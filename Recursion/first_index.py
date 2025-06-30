def find_first_index(arr,i,x):
    if i==len(arr):
        return -1
    if x==arr[i]:
        return i
    return find_first_index(arr,i+1,x)

list = [1,2,3,4,2,5,2,6,5,4,2]
print(find_first_index(list,0,6))