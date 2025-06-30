def find_last_index(arr,i,x):
    if i==len(arr):
        return -1
    idx = find_last_index(arr,i+1,x)
    if x==arr[i] and idx == -1:
        idx = i
    return idx


list = [1,2,3,4,2,5,2,6,5,4,2]
print(find_last_index(list,0,5))
