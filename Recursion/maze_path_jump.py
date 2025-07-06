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

    if dr - sr:  # equivalent to checking if (dr - sc) != 0
        for jump in range(1,dc - sc+1):
            dpaths = get_maze_path_jump(sr+jump, sc + jump, dr, dc)
            for path in dpaths:
                jump_paths.append('d' + str(jump) + path)

    return jump_paths

print(get_maze_path_jump(1,1,2,2))