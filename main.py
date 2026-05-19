print("===== BÀI 1 =====")
so_nguyen = 10
so_thuc = 3.14
chuoi = "Hello Python"
print("Số nguyên:", so_nguyen)
print("Số thực:", so_thuc)
print("Chuỗi:", chuoi)


print("===== BÀI 2 =====")
PI = 3.14
r = 5
chu_vi = 2 * PI * r
print("Bán kính =", r)
print("Chu vi hình tròn =", chu_vi)


print("===== BÀI 3 =====")
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
tong = a + b
hieu = a - b
tich = a * b
print("Tổng =", tong)
print("Hiệu =", hieu)
print("Tích =", tich)
if b != 0:
    thuong = a / b
    print("Thương =", thuong)
else:
    print("Không thể chia cho 0")


print("===== BÀI 4 =====")
def sum_two_numbers(x, y):
    return x + y
ket_qua = sum_two_numbers(5, 7)
print("Tổng hai số là:", ket_qua)

print("===== BÀI 5 =====")
name = "Đức"
age = 19
average_score = 8.5
print("Tên:", name)
print("Kiểu dữ liệu của name:", type(name))
print("Tuổi:", age)
print("Kiểu dữ liệu của age:", type(age))
print("Điểm trung bình:", average_score)
print("Kiểu dữ liệu của average_score:", type(average_score))
age_next_year = age + 1
doubled_score = average_score * 2
print("Tuổi năm sau:", age_next_year)
print("Điểm trung bình nhân đôi:", doubled_score)