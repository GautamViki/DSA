def solve(stack,k):
    if k==1:
        stack.pop()
        return
    temp = stack.pop()
    solve(stack,k-1)
    stack.append(temp)

def remove_mid_from_stack(stack,size):
    if len(stack)==0:
        return stack
    mid_ele = size/2
    solve(stack,int(mid_ele))
    return stack


stack = [1, 2, 3,4,5,6,7,8]
print(remove_mid_from_stack(stack,len(stack)))