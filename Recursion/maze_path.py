def get_maze_path(sr,sc,dr,dc):
    if sr == dr and sc == dc:
        return ['']
    vpaths = []
    hpaths = []
    if sr<dr:
        vpaths = get_maze_path(sr+1,sc,dr,dc)
    if sc<dc:
        hpaths = get_maze_path(sr,sc+1,dr,dc)
    paths = []
    for path in vpaths:
       paths.append('v'+path)
    for path in hpaths:
        paths.append('h'+path)
    return paths

print(get_maze_path(1,1,2,2))