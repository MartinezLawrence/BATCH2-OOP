# Prog06: First number minus all remaining numbers
numbers = []
for i in range(10):
    numbers.append(float(input(f"Enter number {i+1}: ")))
result = numbers[0] - sum(numbers[1:])
print(result)