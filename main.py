#Найдите сумму цифр трехзначного числа.
n = input("Введите трехзначное число: ")
n = int(n)

a = n % 10
b = n % 100 // 10
c = n // 100

print("Сумма цифр числа:", a + b + c)