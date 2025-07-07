def get_maze_path_jump(sr,sc,dr,dc):
    if sc==dc and sr==dr:
        return [""]
    jump_paths = []
    for jump in range(1,dr-sr+1):
        vpaths = get_maze_path_jump(sr+jump,sc,dr,dc)
        for path in vpaths:
            jump_paths.append('v'+str(jump)+path)

    for jump in range(1,dc-sc+1):
        hpaths = get_maze_path_jump(sr,sc+jump,dr,dc)
        for path in hpaths:
            jump_paths.append('h'+str(jump)+path)

    if dr - sr:
        for jump in range(1,dc - sc+1):
            dpaths = get_maze_path_jump(sr+jump, sc + jump, dr, dc)
            for path in dpaths:
                jump_paths.append('d' + str(jump) + path)

    return jump_paths

print(get_maze_path_jump(1,1,2,2))

def print_maze_path_jump(sr,sc,dr,dc,path):
    if sr==dr and sc==dc:
        print(path)
        return
    if sr>dr or sc>dc:
        return
    for jump in range(1,dr-sr+1):
        print_maze_path_jump(sr+jump,sc,dr,dc,path+'v'+str(jump))
    for jump in range(1,dc-sc+1):
        print_maze_path_jump(sr, sc+jump, dr, dc, path+'h'+str(jump))
    if sc<dc:
        for jump in range(1,dr-sr+1):
            print_maze_path_jump(sr+jump, sc+jump, dr, dc, path+'d'+str(jump))

print_maze_path_jump(1,1,2,2,'')