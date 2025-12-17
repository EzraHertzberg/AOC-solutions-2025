
ids = []

def range_to_list(_range):
    global ids
    interval = _range.split("-")
    start, end = interval
    id_maker = int(start)
    while id_maker <= int(end):
        ids.append(str(id_maker))
        id_maker += 1

    
def id_check(value):
    is_valid = True

    str_lst = list(value)

    for i in range(1, ((len(value))//2 + 1)):
        if(len(value) % i == 0):
            parts = []
            for j in range(len(value)//i):
                part_es = []
                for l in range(i):
                    part_es.append(str_lst[l + (j * (i))])
                parts.append(part_es)
        if parts.count(parts[0]) == len(parts):
            is_valid = False
    
    if is_valid:
        return 0
    else:
        return int(value)

#print(id_check("121121121"))
    
total = 0 
with open("input") as f:
    full_text = f.read()
    ranges = full_text.split(",")
    for interval in ranges:
        range_to_list(interval)
    for value in ids:
        total = total + id_check(value)
    print(total)
    
