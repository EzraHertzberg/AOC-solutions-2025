"""
Day 9 solution
"""

numbers = []

with open("input") as f:
    for line in f:
        values = line.strip().split(",")
        for i in range(len(values)):
            values[i] = int(values[i])
        numbers.append(values)

def find_area(point1, point2):
    width = abs(point1[0] - point2[0]) + 1
    height = abs(point1[1] - point2[1]) + 1
    return width * height


max_area = 0
for i in range(len(numbers)):
    for j in  range(i, len(numbers)):
        if numbers[i] != numbers[j]:
            area = find_area(numbers[i], numbers[j])
            if area > max_area:
                max_area = area
print(max_area)