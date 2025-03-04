import pyodbc

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=HOANGPHUC;'
    'DATABASE=QLSinhVien;'
    'UID=h1;'
    'PWD=1'
)
cursor = conn.cursor()

# Thực thi câu truy vấn SELECT
cursor.execute("SELECT * FROM SinhVien")
print('Danh sách sinh viên: ')
# Lấy dữ liệu và hiển thị
rows = cursor.fetchall()
for row in rows:
    print(row)
    print(type(row))
    

# Đóng con trỏ
cursor.close()

