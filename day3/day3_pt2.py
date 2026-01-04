"""
Advent of code day 3 pt 2 solution
"""

exampleinp = "811811111111119"


def max_key(d):
    m_key = -1
    for key in d:
        if key > m_key:
            m_key = key
    return m_key

def scan(line, digits):
    lst_line = list(line)
    joltages = {}
    for i in range(digits):
        largest_val = 0
        val_index = 0
        for i in range(len(lst_line) - digits + i, max_key(joltages), - 1):
            if int(lst_line[i]) >= int(largest_val):
                largest_val = lst_line[i]
                val_index = i
        joltages[val_index] = largest_val

    solution = ""
    for value in joltages.values():
        solution = solution + str(value)
    return int(solution)
    
#print(scan(exampleinp, 2))

_sum = 0

with open("input") as f:
    for line in f:
        line = line.strip()
        _sum += scan(line, 12)


print(_sum)
