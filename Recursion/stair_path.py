def get_stair_path(n):
    if n==0:
        return ['']
    elif n<0:
        return []
    path1 = get_stair_path(n-1)
    path2 = get_stair_path(n-2)
    path3 = get_stair_path(n-3)
    paths = []
    for path in path1:
        paths.append('1'+path)
    for path in path2:
        paths.append('2'+path)
    for path in path3:
        paths.append('3'+path)
    return paths

print(get_stair_path(4))

def print_stair_path(n,ans):
    if n==0:
        print(ans)
        return
    elif n<0:
        return
    print_stair_path(n-1,ans+'1')
    print_stair_path(n-2,ans+'2')
    print_stair_path(n-3,ans+'3')

print_stair_path(4,'')