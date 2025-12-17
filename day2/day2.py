
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
    if(len(value) % 2 == 0):
        str_lst = list(value)
        first_half = []
        for i in range(len(value)//2):
            first_half.append(str_lst.pop(0))
        first_half = "".join(first_half)
        last_half = "".join(str_lst)
        if first_half == last_half:
            is_valid = False
    
    if is_valid:
        return 0
    else:
        return int(value)
        
    


total = 0 
with open("input") as f:
    full_text = f.read()
    ranges = full_text.split(",")
    for interval in ranges:
        range_to_list(interval)
    for value in ids:
        total = total + id_check(value)
    print(total)