i = 5
u = 20
incr = 1
numbers = []

def loop(num, end, incr):
    for y in range(num, end, incr):
        print(f"At the top i is {y}")
        numbers.append(y)
        
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {y}")
loop(i, u, incr)
print("The numbers: ")

for x in numbers:
    print(x)