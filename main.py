n = int(input("Введите число: "))
mas = [i for i in range(n + 1)]
mas[1] = 0
i = 2
while (i<n):
    if(mas[i] != 0):
        j = i + i
        while (j <= n):
            mas[j] = 0
            j = j + i
    i += 1

mas = [i for i in mas if i != 0]
print(mas)