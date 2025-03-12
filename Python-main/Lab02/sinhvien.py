from datetime import datetime
from math import gcd
class SinhVien:
    truong = "Đại học Đà Lạt"
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh
    @property
    def maSo(self):
        return self.__maSo
    @property
    def hoTen(self):
        return self.__hoTen
    @property
    def ngaySinh(self):
        return self.__ngaySinh
    @maSo.setter
    def maSo(self,maSo):
        if self.laMaSoHopLe(maSo):
            self.__maSo = maSo

    @staticmethod
    def laMaSoHopLe(maSo : int):
        return len(str(maSo)) == 7
    
    @staticmethod
    def doiTenTruong(self,tenMoi):
        self.truong = tenMoi

    def __str__(self) -> str:
        return f"{self.maSo}\t{self.hoTen}\t{self.__ngaySinh}"
    
    def xuat(self):
        print(f"{self.maSo}\t{self.hoTen}\t{self.__ngaySinh}")
class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []

    def themSinhVien(self, sv:SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSvTheoMssv(self, mssv:int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1
    
    def XoaSvTheoMssv(self, maSo:int)-> bool:
        vt = self.timSvTheoMssv(maSo)
        if vt!= -1:
            del self.dssv[vt]
            return True
        else:
            return False
        
    def timSvTheoTen(self,ten:str):
         return [sv for sv in self.dssv if ten.lower() in sv.lower()]

    def timSvSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh < ngay]
    
    def docDanhSachTuFileTXT(self, tenFile: str):
        with open(tenFile, mode='r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split("\t") 
                if len(parts) == 3:
                        maSo = int(parts[0])  
                        hoTen = ' '.join(parts[1:-1])  
                        ngaySinh = datetime.strptime(parts[-1], "%Y-%m-%d")  
                        sv = SinhVien(maSo, hoTen, ngaySinh)
                        self.themSinhVien(sv)                

    def sapXepGiam(self, giamDan=False):
        self.dssv.sort(key=lambda sv: sv.hoTen, reverse=giamDan)
    def sapXepTang(self, tangDan=True):
        self.dssv.sort(key=lambda sv: sv.hoTen, reverse=tangDan)

# danhSach = DanhSachSv()
# danhSach.docDanhSachTuFileTXT('sinhvien.txt')
# print("Danh sách sinh viên trước khi sắp xếp:")
# danhSach.xuat()
# print("Danh sách sinh viên sau khi sắp xếp:")
# danhSach.sapXepTang()
# danhSach.xuat()

class PhanSo:
    def __init__(self,tu_so: int, mau_so: int) -> None:
        if mau_so == 0:
            raise ValueError("Mẫu số không thể bằng 0")
        self.tu_so = tu_so
        self.mau_so = mau_so
        self.rut_gon()
        
    def rut_gon(self):
        ucln = gcd(self.tu_so,self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln
        if self.mau_so < 0:
            self.tu_so = -self.tu_so
            self.mau_so = -self.mau_so

    def __add__(self, other):
        tu = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau)

    def __sub__(self, other):
        tu = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau)

    def __mul__(self, other):
        tu = self.tu_so * other.tu_so
        mau = self.mau_so * other.mau_so
        return PhanSo(tu, mau)

    def __truediv__(self, other):
        if other.tu_so == 0:
            raise ZeroDivisionError("Không thể chia cho 0.")
        tu = self.tu_so * other.mau_so
        mau = self.mau_so * other.tu_so
        return PhanSo(tu, mau)

    def __str__(self):
        if self.mau_so == 1:
            return f"{self.tu_so}"
        return f"{self.tu_so}/{self.mau_so}"
   
a = PhanSo(1,6)
# a.tu_so = 2
# a.mau_so = 3
b = PhanSo(4,12)
print(f"{a}+{b}={a+b}")
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")
