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
        grid.append(line)

def adjacency_check(grid, x, y):
    internal_counter = 0
    if grid[y][x] == "@":
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if(dx + x >= 0 and dy + y >= 0 and dy + y < len(grid) and dx + x < len(grid[y])):
                    if dy != 0 or dx != 0:
                       if(grid[y + dy][x + dx] == "@"):
                           internal_counter += 1
            
        if internal_counter < 4:
            return 1
        else:
            return 0
    else:
        return 0

total = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        total = total + adjacency_check(grid, i, j)
print(total)

#print(adjacency_check(grid, 2, 0))





'''
        print("regonized")
        try:
            if grid[y - 1][x - 1] == "@":
                internal_counter += 1
        except:
            pass
        
        try:
            if grid[y - 1][x] == "@":
                internal_counter += 1
        except:
            pass
        
        try:
            if grid[y - 1][x + 1] == "@":
                internal_counter += 1
        except:
            pass

        try:
            if grid[y][x - 1] == "@":
                internal_counter += 1
        except:
            pass
        try:
            if grid[y][x + 1] == "@":
                internal_counter += 1
        except:
            pass
        try:
            if grid[y + 1][x - 1] == "@":
                internal_counter += 1
        except:
            pass
        try:
            if grid[y + 1][x] == "@":
                internal_counter += 1
        except:
            pass  
        try:
            if grid[y + 1][x + 1] == "@":
                internal_counter += 1
        except:
            pass
        print(internal_counter)
'''