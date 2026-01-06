"""
Advent of Code day 5 pt 2 solution
"""

valid_ids = []

def fresh_check(domain):
    minimum, maximum = domain.split("-")
    minimum = int(minimum)
    maximum = int(maximum)
    print(minimum)
    print(maximum)
    for i in range(minimum, maximum):
        if i not in valid_ids:
            valid_ids.append(i)


total = 0
with open("input") as f:
    full_text = f.read()
    information = full_text.split("\n\n")
    domains = information[0].split("\n")
    numbers = information[1].split("\n")
    numbers.pop()

    z = 0
    for domain in domains:
        z = z + 1
        print(z)
        fresh_check(domain)

print(len(valid_ids))
