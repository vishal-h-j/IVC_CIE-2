n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    num = int(input())
    arr.append(num)

if arr == arr[::-1]:
    print("Perfect Array")
else:
    print("Not a Perfect Array")