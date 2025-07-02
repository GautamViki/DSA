def get_keyboard_combinations(str1,str2,i,res):
    if i==len(str1):
        return res
    char1=str1[i]
    for char2 in str2:
        res.append(char1+char2)
    return get_keyboard_combinations(str1,str2,i+1,res)

keyboard_dict={
    1:"abc",
    2:"def",
    3:"ghi",
    4:"jkl",
    5:"mno",
    6:"pqr",
    7:"stu",
    8:"vwx",
    9:"yz",
    0:"?!"
}
pressed_key=12
arr = []
while pressed_key>0:
    n=pressed_key%10
    arr.append(n)
    pressed_key = pressed_key/10
print(arr)
i=0
j=len(arr)-1
while i<j:
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    i=i+1
    j=j-1

print("-----",arr)
# res=get_keyboard_combinations(keyboard_dict.get(arr[1]),keyboard_dict.get(arr[2]),0,[])
# print(res)
