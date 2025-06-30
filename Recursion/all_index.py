def find_all_index(array, i, x):
    if i==len(array):
        return []
    arr = find_all_index(array, i + 1, x)
    if x==array[i]:
        arr.append(i)
    return arr

def find_all_index_I(arr ,i,x,res):
    if i==len(arr):
        return res
    if x==arr[i]:
        res.append(i)
    return find_all_index_I(arr,i+1,x,res)

list = [1,2,3,4,2,5,2,6,5,4,2]
print(find_all_index(list,0,2))
print(find_all_index_I(list,0,2,[]))
