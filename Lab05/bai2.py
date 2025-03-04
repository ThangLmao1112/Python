import tkinter as tk
from tkinter import ttk
import pyodbc

# Dữ liệu mẫu cho danh sách món ăn
ds_mon_an = []

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=HOANGPHUC;'
    'DATABASE=QLMonAn;'
    'UID=h1;'
    'PWD=1'
)
cursor = conn.cursor()

# Thực thi câu truy vấn SELECT
cursor.execute("select MaMonAn,TenMonAn,DonViTinh,DonGia,TenNhom from MonAn, NhomMonAn " +
"where MonAn.Nhom=NhomMonAn.MaNhom")
print('Danh sách món ăn: ')
# Lấy dữ liệu và hiển thị
rows = cursor.fetchall()
for row in rows:
   ds_mon_an.append({"Ma": row[0], "Ten": row[1], "DonVi": row[2], "DonGia": row[3], "Nhom": row[4]})
    

# Đóng con trỏ
cursor.close()



# Hàm tải dữ liệu vào Treeview
def load_data(nhom="Tất cả"):
    for item in tree.get_children():
        tree.delete(item)
    
    for mon_an in ds_mon_an:
        if nhom == "Tất cả" or mon_an["Nhom"] == nhom:
            tree.insert("", "end", values=(mon_an["Ma"], mon_an["Ten"], mon_an["DonVi"], mon_an["DonGia"], mon_an["Nhom"]))

# Hàm khi chọn nhóm trong ComboBox
def on_combobox_select(event):
    selected_nhom = cbo_nhom.get()
    load_data(selected_nhom)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý món ăn")
root.geometry("800x400")

# Tiêu đề
lbl_title = tk.Label(root, text="Nhóm món ăn", font=("Arial", 14))
lbl_title.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# ComboBox chọn nhóm món ăn
cbo_nhom = ttk.Combobox(root, state="readonly", font=("Arial", 12))
cbo_nhom['values'] = ("Tất cả", "Khai vị", "Hải sản", "Bia - Nước ngọt")
cbo_nhom.current(0)
cbo_nhom.grid(row=0, column=1, padx=10, pady=10)
cbo_nhom.bind("<<ComboboxSelected>>", on_combobox_select)

# Treeview hiển thị danh sách món ăn
tree = ttk.Treeview(root, columns=("Ma", "Ten", "DonVi", "DonGia", "Nhom"), show="headings")
tree.heading("Ma", text="Mã món ăn")
tree.heading("Ten", text="Tên món ăn")
tree.heading("DonVi", text="Đơn vị tính")
tree.heading("DonGia", text="Đơn giá")
tree.heading("Nhom", text="Nhóm")
tree.column("Ma", width=80, anchor="center")
tree.column("Ten", width=200)
tree.column("DonVi", width=100, anchor="center")
tree.column("DonGia", width=120, anchor="center")
tree.column("Nhom", width=150, anchor="center")
tree.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Thanh cuộn cho Treeview
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.grid(row=1, column=4, sticky="ns")

# Load dữ liệu ban đầu
load_data()

# Chạy giao diện
root.mainloop()
