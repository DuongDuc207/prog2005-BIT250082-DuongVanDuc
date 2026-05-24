print(" bài 1")
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
n=int(input("nhập n :"))
print (is_even(n))


print("BÀi 2")
a = float(input("nhập số a:"))
b = float(input("nhập số b:"))
c = float(input("nhập số c:"))
print("số lớn nhất trong ba số",a,b,c,"là:",max(a,b,c))


print("bài 3")
def greet(name="Student"):
    print(f"Hello, {name}!")
greet()
greet("Duc")


print("Bài 4")
age = int(input("Nhap tuoi: "))
if 1 <= age <= 120:
    print("Tuoi hop le")
else:
    print("Tuoi khong hop le")


print("Bài 5")
text = input("Nhap chuoi: ")
tong=0
for i in text:
    if i == "a":
        tong += 1
print("Số lần xuất hiện a là:", tong)



print("Bài 6")
celsius = float(input("Nhap nhiet do C: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"Nhiet do F = {fahrenheit:.2f}")


print("Bài 7")
weight = float(input("Nhap can nang (kg): "))
height = float(input("Nhap chieu cao (m): "))
bmi = weight / (height * height)
print(f"BMI = {bmi:.2f}")



print("Bài 8")
try:
    x = int(input("Nhap so thu nhat: "))
    y = int(input("Nhap so thu hai: "))
    result = x / y
    print("Ket qua =", result)
except ZeroDivisionError:
    print("Loi: Khong the chia cho 0")
except ValueError:
    print("Loi: Du lieu khong hop le")


print("Bài 9")
import math
number = float(input("Nhap so: "))
if number < 0:
    print("Khong tinh duoc can bac hai cua so am")
else:
    print("Can bac hai =", math.sqrt(number))


print("Bài 10")
for i in range(1, 4):
print(f"\nSinh vien {i}")
name = input("Nhap ten: ")
Toán = float(input("Nhap diem Toan: "))
Lý = float(input("Nhap diem Ly: "))
Hóa = float(input("Nhap diem Hoa: "))
average = (Toán + Lý + Hóa) / 3
print("Ten:", name)
print(f"Diem trung binh: {average:.2f}")
