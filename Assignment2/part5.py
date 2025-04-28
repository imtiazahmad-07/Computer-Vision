# (f) Print the following using for loop
# 12345
# 1234
# 123
# 12

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end="")
    print()
