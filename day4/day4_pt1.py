"""
Advent of code day 4 pt 1 solution
"""
"""
grid = [
"..@@.@@@@.",
"@@@.@.@.@@",
"@@@@@.@.@@",
"@.@@@@..@.",
"@@.@@@@.@@",
".@@@@@@@.@",
".@.@.@.@@@",
"@.@@@.@@@@",
".@@@@@@@@.",
"@.@.@@@.@."  
    ]


"""
grid = []

with open("input") as f:
    for line in f:
        line = line.strip()
        lst_line = list(line)
        grid.append(lst_line)


removed1 = True

def adjacency_check(grid, x, y):
    global removed1
    internal_counter = 0
    if grid[y][x] == "@":
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if(dx + x >= 0 and dy + y >= 0 and dy + y < len(grid) and dx + x < len(grid[y])):
                    if dy != 0 or dx != 0:
                       if(grid[y + dy][x + dx] == "@"):
                           internal_counter += 1
            
        if internal_counter < 4:
            grid[y][x] = "."
            removed1 = True
            return 1
        else:
            return 0
    else:
        return 0

total = 0

while removed1:
    removed1 = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            total = total + adjacency_check(grid, i, j)
    print(total)





