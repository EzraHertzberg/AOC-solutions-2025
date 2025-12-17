
moving_number = 50

count = 0
pass_zero_count = 0

def number_modify(inp):
    global moving_number, pass_zero_count
    direction = inp[0]
    list_inp = list(inp)
    list_inp.pop(0)
    modifying_number = int("".join(list_inp))
    
    if direction == "L":
        net_number = moving_number - modifying_number
    if direction == "R":
        net_number = moving_number + modifying_number



    if net_number <= 0:
        if (moving_number > 0):
            pass_zero_count = pass_zero_count + 1 + (abs(net_number)//100)
        else:
            pass_zero_count = pass_zero_count + (abs(net_number)//100)
    else:
        pass_zero_count = pass_zero_count + (net_number//100)
    
    
    
    if net_number >= 0:
        moving_number = net_number % 100
    else:
        new_num = 100 - ((abs(net_number)) % 100)
        if new_num == 100:
            new_num = 0
        moving_number = new_num
    


#print(pass_zero_count)

"""

test = [
"L68",
"L30",
"R48",
"L5",
"R60",
"L55",
"L1",
"L99",
"R14",
"L82"]


for val in test:
    number_modify(val)
print(pass_zero_count)
"""
with open("_input") as f:
    for line in f:
        number_modify(line)
        if(moving_number == 0):
            count = count + 1
    print(pass_zero_count)


