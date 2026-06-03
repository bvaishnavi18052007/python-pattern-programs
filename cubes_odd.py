# Convert Odd Numbers in a List to Their Cubes

n = int(input("Enter number of elements in the list: "))

numbers = []

for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    numbers.append(num)

result = []

for num in numbers:
    if num % 2 != 0:
        result.append(num ** 3)

print("\nOriginal List:", numbers)
print("Cubes of Odd Numbers:", result)
