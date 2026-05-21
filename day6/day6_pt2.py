"""
Advent of Code day 6 pt 2 solution
"""
values = []

def calc_result(vals):
    result = int(vals[0])
    if vals[-1] == "*":
        for i in range(len(vals) - 2):
            result = result * int(vals[i + 1])
    else:
        for i in range(len(vals) - 2):    
            result = result + int(vals[i + 1])
    return result

total = 0

equations = []

with open("input") as f:
    lines = f.readlines()

    slines = []
    for line in lines:
        slines.append(line.replace("\n", ""))
    lines = slines


    signs = lines[4].split()
    for sign in signs:
        equations.append([])
    counter = 0
    for i in range(len(lines[0]) - 1, -1, -1):
        val1 = ""
        val2 = "" 
        val3 = ""
        val4 = ""
        val5 = ""
        if lines[0][i] != " ":
            val1 = lines[0][i]
        if lines[1][i] != " ":
            val2 = lines[1][i]
        if lines[2][i] != " ":
            val3 = lines[2][i]
        if lines[3][i] != " ":
            val4 = lines[3][i]
        if lines[4][i] != " ":
            val5 = lines[4][i]    
        num = val1 + val2 + val3 + val4
        

        if num != "":
            equations[counter].append(num)
            pass
        if val5 != "":
            equations[counter].append(val5)
            counter += 1
    for equation in equations:
        total = total + calc_result(equation)
print(total)