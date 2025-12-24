exampleinp = "811111111111119"

def scan(line):
    lst_line = list(line)
    val1 = 0
    val1_index = 0
    val2 = 0    
    for i in range(len(lst_line) - 2, -1, - 1):
        if int(lst_line[i]) >= int(val1):
            val1 = lst_line[i]
            val1_index = i
    for i in range(val1_index + 1, len(lst_line)):
        if int(lst_line[i]) > int(val2):
            val2 = lst_line[i]
    return int(str(val1) + str(val2))
    
print(scan(exampleinp))

_sum = 0
with open("input") as f:
    for line in f:
        line = line.strip()
        _sum += scan(line)
        
print(_sum)
