# Prog07: Print count of even numbers
evens = 0
for _ in range(10):
    if int(float(input("Enter a number: "))) % 2 == 0:
        evens += 1
print(evens)