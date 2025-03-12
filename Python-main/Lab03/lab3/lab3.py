import math
from collections import Counter

def tao_danh_sach():
    return [12, 15, 7, 30, 19, 23, 50, 8, 5, 3]

def so_le_khong_chia_het_cho_5(lst):
    return [x for x in lst if x % 2 == 1 and x % 5 != 0]

def la_fibonacci(n):
    return math.isqrt(5 * n * n + 4) ** 2 == 5 * n * n + 4 or math.isqrt(5 * n * n - 4) ** 2 == 5 * n * n - 4

def cac_so_fibonacci(lst):
    return [x for x in lst if la_fibonacci(x)]

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def so_nguyen_to_lon_nhat(lst):
    primes = [x for x in lst if la_so_nguyen_to(x)]
    return max(primes) if primes else None

def so_fibonacci_nho_nhat(lst):
    fibs = cac_so_fibonacci(lst)
    return min(fibs) if fibs else None

def trung_binh_so_le(lst):
    odds = [x for x in lst if x % 2 == 1]
    return sum(odds) / len(odds) if odds else 0

def tich_so_le_khong_chia_het_cho_3(lst):
    result = 1
    for x in lst:
        if x % 2 == 1 and x % 3 != 0:
            result *= x
    return result

def hoan_doi_phan_tu(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    return lst

def dao_nguoc_danh_sach(lst):
    return lst[::-1]

def so_lon_thu_hai(lst):
    unique_vals = list(set(lst))
    unique_vals.sort(reverse=True)
    return unique_vals[1] if len(unique_vals) > 1 else None

def tong_cac_chu_so(lst):
    return sum(sum(int(digit) for digit in str(abs(x))) for x in lst)

def dem_so_lan_xuat_hien(lst, num):
    return lst.count(num)

def cac_so_xuat_hien_n_lan(lst, n):
    counter = Counter(lst)
    return [num for num, count in counter.items() if count == n]

def cac_so_xuat_hien_nhieu_nhat(lst):
    counter = Counter(lst)
    max_count = max(counter.values())
    return [num for num, count in counter.items() if count == max_count]

# Bài 2 - Hàm đệ quy
def tong_n_so_nguyen_dau_tien(n):
    return n + tong_n_so_nguyen_dau_tien(n - 1) if n > 0 else 0

def giai_thua(n):
    return 1 if n == 0 else n * giai_thua(n - 1)

def fibonacci(n):
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)

def tong_n_so_fibonacci(n):
    return sum(fibonacci(i) for i in range(n))

def tong_can_bac_hai(n):
    return math.sqrt(n) + tong_can_bac_hai(n - 1) if n > 0 else 0

def main():
    lst = tao_danh_sach()
    print("Danh sách:", lst)
    print("Số lẻ không chia hết cho 5:", so_le_khong_chia_het_cho_5(lst))
    print("Các số Fibonacci:", cac_so_fibonacci(lst))
    print("Số nguyên tố lớn nhất:", so_nguyen_to_lon_nhat(lst))
    print("Số Fibonacci nhỏ nhất:", so_fibonacci_nho_nhat(lst))
    print("Trung bình số lẻ:", trung_binh_so_le(lst))
    print("Tích số lẻ không chia hết cho 3:", tich_so_le_khong_chia_het_cho_3(lst))
    print("Danh sách đảo ngược:", dao_nguoc_danh_sach(lst))
    print("Số lớn thứ hai:", so_lon_thu_hai(lst))
    print("Tổng các chữ số trong danh sách:", tong_cac_chu_so(lst))
    print("Các số xuất hiện nhiều nhất:", cac_so_xuat_hien_nhieu_nhat(lst))
    print("Tổng 5 số nguyên đầu tiên:", tong_n_so_nguyen_dau_tien(5))
    print("Giai thừa của 5:", giai_thua(5))
    print("Fibonacci(5):", fibonacci(5))
    print("Tổng 5 số Fibonacci đầu tiên:", tong_n_so_fibonacci(5))
    print("Tổng căn bậc hai của 2 số nguyên đầu tiên:", tong_can_bac_hai(5))

if __name__ == "__main__":
    main()
