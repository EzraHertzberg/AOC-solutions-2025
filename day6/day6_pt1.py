
values = []

def calc_result(vals, i):
    if vals[4][i] == "*":
        result = int(vals[0][i]) * int(vals[1][i]) * int(vals[2][i]) * int(vals[3][i])
    else:
        result = int(vals[0][i]) + int(vals[1][i]) + int(vals[2][i]) + int(vals[3][i])
    return result

total = 0

with open("input") as f:
    for line in f:
        values.append(line.split())
    for i in range(len(values[0])):
        total = total + calc_result(values, i)
    print(total)