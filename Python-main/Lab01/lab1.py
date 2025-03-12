import math
import sys


# 1. Formatted Twinkle Poem
def twinkle_poem():
    print("Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\n Twinkle, twinkle, little star,\n\t How I wonder what you are")


# 2. Python Version Checker
def python_version():
    import sys
    print("     Python Version")
    print(sys.version)
    print("     Version Info")
    print(sys.version_info)


# 3. Current Date and Time
def current_date_time():
    import datetime
    now = datetime.datetime.now()
    print("Current Date and Time: ")
    print(now)

# 4. Area of Circle
def area_of_circle(radius):

    area = math.pi * radius ** 2
    print("Area of Circle with r = ", radius, " => area = ", area)
# area_of_circle(1)

# 5. Reverse Full Name
def reverse_full_name(first_name, last_name):
    print(last_name, first_name)
# reverse_full_name("John", "Doe")

#6. List and Tuple Generator
def list_tuple_generator():
    values = input("Input some comma separated numbers: ")
    list = values.split(",")
    tuple1 = tuple(list)
    print("List: ", list)
    print("Tuple: ", tuple1)
# list_tuple_generator()

# 7. File Extension Extractor
def file_extension_extractor():
    filename = input("Input the Filename: ")
    extension = filename.split(".")
    print("The extension of the file is: ", extension[-1])


# 1. Tính:
def add(a, b):
    return a+b

def chia(a, b):
    return a/b

def mu(a, b):
    return a**b

# 2. Tính diện tích hình chữ nhật khi biết bán kính
def dien_tich_hinh_chu_nhat(a, b):
    return a*b

def dien_tinh_hinh_tron(r):
    return 3.14*r*r

# 3. Xuất tất cả các số nguyên tố trong 1 khoảng cho trước
def Array_prime(n):
    if n < 2:
        return []
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num)):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
   
# print(Array_prime(100))

# 4. Kiểm tra 1 số nguyên n có phải là số Fibonacci hay không
def KtraFibonacci(n):
    a=0
    b=1
    while(b<n):
        (a,b)=(b,a+b)
        if(b==n):
            return True
    return False

# print(array(9))

# 5. Tìm số Fibonacci thứ n (dùng đệ quy và không đệ quy)
def tim_so_fibonacci_thu_n(n):
    if n <= 0:    
        return 0
    elif n == 1:
        return 1
    else:
        return tim_so_fibonacci_thu_n(n - 1) + tim_so_fibonacci_thu_n(n - 2)  


def tim_so_fibonacci_thu_n_khong_de_quy(n):
    a=0
    b=1
   
    for i in range(2,n+1):
        a,b=b,a+b
        
    return b

# 6. Tính tổng n số Fibonacci đầu tiên (dùng đệ quy và không đệ quy) 
def tim_tong_fibonacci_thu_n_khong_de_quy(n):
    a=0
    b=1
    tong =1
    for i in range(1,n):
        a,b=b,a+b
        tong+=b
    return tong


def tong_fibonacci_de_quy(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return tim_so_fibonacci_thu_n(n) + tong_fibonacci_de_quy(n - 1)

# 7. Tính tổng căn bậc 2 của n số nguyên đầu tiên
def tong_can_bac_2(n):
    tong = 0
    for i in range(1,n+1):
        tong+=i**0.5
    return tong

# print(tong_can_bac_2(5))

# 8. Giải phương trình bậc 2: ax2 + bx + c=0 
def giai_phuong_trinh_bac_2(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b/(2*a)
        return "Phương trình có nghiệm kép x = ", x
    else:
        x1 = (-b + delta**0.5)/(2*a)
        x2 = (-b - delta**0.5)/(2*a)
        return "Phương trình có 2 nghiệm phân biệt x1 = ", x1, " và x2 = ", x2

# print(giai_phuong_trinh_bac_2(3, 4, 1))

# 9. Tính n! 
def tinh_giai_thua(n):
    if n == 0:
        return 1
    return n*tinh_giai_thua(n-1)

# 10. In * dạng tam giác dưới như hình bên, đầu vào là số hàng(cột)
def in_hinh_tam_giac(n):
    for i in range(1,n):
        for j in range(1,i+1):
            if j == 1 or j == i:
                print("* ", end="")
            else:
                print("  ", end="")     
        print()
    print("* "*n) 

# print(in_hinh_tam_giac(10))

# 11.   Đổi giờ - phút – giây: thời gian đầu vào là giây được đổi thành giờ, phút, giây. 
# Xuất kết quả ra màn hình dưới dạng: giờ:phút:giây. Ví dụ: soGiay = 3770 thì xuất 
# ra màn hình 1:2:50. 

def doi_gio_phut_giay(so_giay):
    gio = so_giay//3600
    phut = (so_giay%3600)//60
    giay = (so_giay%60)
    return str(gio)+":"+str(phut)+":"+str(giay)
# print(doi_gio_phut_giay(3770))

# 12. Cho một mảng số nguyên: 
array = [1, 2, 3, 9, 4, 11, 6, 7, 8, 10]
print(array)
# a) Xuât tất cả các số lẻ không chia hết cho 5 
def so_le_khong_chia_het_cho_5(array):
    ket_qua = []
    for i in array:
        if i%2 != 0 and i%5 != 0:
            ket_qua.append(i)
    return ket_qua
# print(so_le_khong_chia_het_cho_5(array))

# b) Xuất tất cả các số Fibonacci 
def so_fibonacci(array):
    ket_qua = []
    for i in array:
        if KtraFibonacci(i):
            ket_qua.append(i)
    return ket_qua
# print(so_fibonacci(array))

# c) Tìm số nguyên tố lớn nhất 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def so_nguyen_to_lon_nhat(array):
    max =  -sys.maxsize
    
    for i in array:
        if is_prime(i) and (i > max):
            max = i
    return max
# print(so_nguyen_to_lon_nhat(array))

# d) Tìm số Fibonacci bé nhất 
def so_fibonacci_be_nhat(array):
    min = sys.maxsize
    for i in array:
        if KtraFibonacci(i) and i< min:
            min = i
    return min
# print(so_fibonacci_be_nhat(array))


# e) Tính trung bình các số lẻ 
def trung_binh_so_le(array):
    tong = 0
    dem = 0
    for i in array:
        if i%2 != 0:
            tong+=i
            dem+=1
    return tong/dem
print(trung_binh_so_le(array))

# f) Tính tích các phần tử là số lẻ không chia hết cho 3 trong mảng 
def tich_so_le_ko_chia_het_cho_3(array):
    tich = 1
    for i in array:
        if i%2 != 0 and i%3 != 0:
            tich*=i
    return tich

# g) Đổi chỗ 2 phần tử của danh sách, đầu vào là 2 vị trí cần đổi chỗ 
def doi_cho_2_phan_tu(array, i, j):
    array[i], array[j] = array[j], array[i]

# h) Đảo ngược trật tự các phần tử của danh sách
def dao_nguoc(array):
    l=0
    r=len(array)-1
    while l<r:
        array[l],array[r]=array[r],array[l]
        l+=1
        r-=1
    return array

def dao_nguoc_v2(array):
    return array[::-1]

# i) Xuất tất cả các số lớn thứ nhì của danh sách
def so_lon_thu_2(array):
    max1 = max2 = -sys.maxsize
    for i in array:
        if i > max1:
            max2 = max1
            max1 = i
       
    return max2

print (so_lon_thu_2(array))


        
    
            











