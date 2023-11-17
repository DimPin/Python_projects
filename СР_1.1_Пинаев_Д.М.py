def simpleNum(n):
    k = 0
    for i in range(2, n // 2+1):
        if (n % i == 0):
            k = k+1
    if (k <= 0):
        return True
    else:
        return False

num = int(input("Введите число: "))
arr = []

for i in range(1, num+1):
    if(simpleNum(i)):
        arr.append(i)

print(arr)