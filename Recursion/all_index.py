def find_all_index(array, i, x):
    if i==len(array):
        return []
    arr = find_all_index(array, i + 1, x)
    if x==array[i]:
        arr.append(i)
    return arr

list = [1,2,3,4,2,5,2,6,5,4,2]
print(find_all_index(list,0,5))