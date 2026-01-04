boxes = []

with open("input") as f:
    for line in f:
        values = line.strip().split(",")
        for i in range(len(values)):
            values[i] = int(values[i])
        boxes.append(values)

circuts = []

def check_distance(box1, box2):
    return ((box2[0]- box1[0])**2 + (box2[1] - box1[1])**2 + (box2[2] - box1[2])**2) ** 0.5

def is_in_same_circut(box1, box2):
    for circut in circuts:
        if box1 in circut and box2 in circut:
            return True
    return False


def find_closest_valid_pair():
    smallest_dist = 10000000000
    closest_pair = []
    for i in range(len(boxes)):
        for j in range(i, len(boxes)):
            if not is_in_same_circut(boxes[i], boxes[j]) and boxes[i] != boxes[j]:
                if check_distance(boxes[i], boxes[j]) < smallest_dist:
                    closest_pair = [boxes[i], boxes[j]]
                    smallest_dist = check_distance(boxes[i], boxes[j])
    return closest_pair
            
            
def connect_circuts(box1, box2):
    circ1 = []
    circ2 = []
    
    for circut in circuts:
        if box1 in circut:
            circ1 = circut
        if box2 in circut:
            circ2 = circut
    if not circ1:
        circ1 = [box1]
    else:
        circuts.remove(circ1)
    if not circ2:
        circ2 = [box2]
    else:
        circuts.remove(circ2)
    circuts.append(circ1 + circ2)

for i in range(999):
    if i == 1:
        print("we iterated through once")
    if i % 2 == 0:
        print(f"made it to {i} iteration milestone")
    
    box1, box2 = find_closest_valid_pair()
    connect_circuts(box1, box2)


def get_len(e):
    return len(e)
circuts.sort(reverse = True, key = get_len)

print(len(circuts[0]) * len(circuts[1]) * len(circuts[2]))
