grid = []
split_count = 0
with open("input") as f:
    for line in f:
        grid.append(list(line))
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                print("S")
                grid[y + 1][x] = "|"
            
            if grid[y][x] == "|" and y < len(grid) - 1:
                if grid[y + 1][x] == "^":
                    split_count += 1
                    grid[y + 1][x - 1 ] = "|"
                    grid[y + 1][x + 1 ] = "|"
                else:
                    grid[y + 1][x] = "|"
           
print(split_count)