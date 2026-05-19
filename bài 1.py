print("Bài 1")
n=1
a = 32.5
b ="hello world"
print ("số nguyên là: ",n)
print("số thực là:",a)
print("chuỗi là:",b)


print("Bài 2")
Pi = 3.14
r = 5
print("chu vi là:",2*Pi*r)


print("Bài 3")
a=int(input("số nguyên a:"))
b=int(input("số nguyên b:"))
print ("Tổng",a+b)
print ("hiệu",a-b)
print ("Tích",a*b)
if b == 0:
    print("lỗi phép tính mời nhập lại")
else:
    print("Thương",a/b)


print("Bài 4")
def  sum_two_numbers(a, b):
    return a+b
kq=sum_two_numbers(4,7)
print("Tổng",kq)


print("Bài 5")
name="Duc dz"
age= 18
average_score = 7.3
print("Tên:", name)
print("Kiểu dữ liệu của name:", type(name))
print("Tuổi sau khi +1",age+1)
print("Kiểu dữ liệu của age:", type(age))
print(" doubled_score",average_score*2)
print("Kiểu dữ liệu của average_score:", type(average_score))