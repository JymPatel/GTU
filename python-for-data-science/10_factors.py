number = int(input("enter number: "))

print("factors: ", end="")
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")
