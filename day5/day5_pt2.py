"""
Advent of Code day 5 pt 2 solution
First thing I've coded over first college summer break
Interesting start
"""

valid_ids = []

fr_ranges = []
total = 0

def fresh_check(domain):
    global total
    minimum, maximum = domain.split("-")
    minimum = int(minimum)
    maximum = int(maximum)

    size = (maximum - minimum) + 1

    nr_min = minimum
    nr_max = maximum
    
    ranges_to_delete = []

    for fr_range in fr_ranges:

        o_min = fr_range[0]
        o_max = fr_range[1]
        if o_min > maximum or o_max < minimum:
            pass
        elif o_min >= minimum and o_max <= maximum:
            ranges_to_delete.append(fr_range)
            size = size - ((o_max - o_min) + 1)
        elif(o_max >= maximum and o_min <= minimum):
            ranges_to_delete.append(fr_range)
            size = 0
            nr_min = o_min
            nr_max = o_max
        elif o_min >= minimum and o_min <= maximum and o_max > maximum:
            ranges_to_delete.append(fr_range)
            nr_max = o_max
            size = size - ((maximum - o_min) + 1)
        elif o_max >= minimum and o_max <= maximum and o_min <= minimum:
            nr_min = o_min
            ranges_to_delete.append(fr_range)
            size = size - ((o_max - minimum) + 1)

    fr_ranges.append((nr_min, nr_max))

    for fr_range in ranges_to_delete:
        fr_ranges.remove(fr_range)
    total = total + size



total = 0


with open("input") as f:
    full_text = f.read()
    information = full_text.split("\n\n")
    domains = information[0].split("\n") 
    for domain in domains:
        fresh_check(domain)


print(total)
