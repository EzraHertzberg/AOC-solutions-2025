def fresh_check(domain, ing):
    minimum, maximum = domain.split("-")
    ing = int(ing)
    minimum = int(minimum)
    maximum = int(maximum)
    if ing >= minimum and ing <= maximum:
        return True
    else:
        return False


total = 0
with open("input") as f:
    full_text = f.read()
    information = full_text.split("\n\n")
    domains = information[0].split("\n")
    numbers = information[1].split("\n")
    numbers.pop()

    for number in numbers:
        for domain in domains:
            if fresh_check(domain, number):
                total += 1
                break
print(total)
