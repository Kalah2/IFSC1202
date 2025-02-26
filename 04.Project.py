height = int(input("Enter maximum height: "))
for i in range(1, height + 1):
    print("* " * i)

for i in range(height - 1, 0, -1):
    print("* " * i)