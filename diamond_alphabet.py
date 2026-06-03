# Alphabet Diamond Pattern

rows = int(input("Enter number of rows: "))

# Upper Half
for i in range(1, rows + 1):
    for s in range(rows - i):
        print(" ", end="")

    ch = 65  # ASCII value of 'A'

    for j in range(1, 2 * i):
        print(chr(ch), end="")

        if j < i:
            ch += 1
        else:
            ch -= 1

    print()

# Lower Half
for i in range(rows - 1, 0, -1):
    for s in range(rows - i):
        print(" ", end="")

    ch = 65

    for j in range(1, 2 * i):
        print(chr(ch), end="")

        if j < i:
            ch += 1
        else:
            ch -= 1

    print()
