def insert_in_sorted_list(arr,ele):
    if len(arr)==0 or arr[len(arr)-1]<=ele:
        arr.append(ele)
        return arr
    last_ele = arr.pop()
    sorted_arr = insert_in_sorted_list(arr,ele)
    sorted_arr.append(last_ele)
    return sorted_arr

def sort_list(arr):
    if len(arr)==1:
        return arr
    last_ele = arr.pop()
    new_arr= sort_list(arr)
    sorted_arr= insert_in_sorted_list(new_arr,last_ele)
    return sorted_arr

arr= [3,2,1,0,5,-1]
print(sort_list(arr))
