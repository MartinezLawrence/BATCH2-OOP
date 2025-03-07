# Prog10: Print all numbers between two input numbers
a, b = map(int, input("Enter two numbers: ").split())
for i in range(min(a, b) + 1, max(a, b)):
    print(i, end=" ")