import sqlite3
import pyodbc

def get_connection():
    connection = sqlite3.connect('QLSinhVien.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("select sqlite_version();")
        db_version = cursor.fetchone()
        print("Bạn đang sử dụng SQLite phiên bản: ", db_version)
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Đã có lỗi xảy ra. Thông tin lỗi: ", error)

read_database_version()
connectionString = '''DRIVER={SQL Server};
                      SERVER=.;DATABASE=QLSinhVien;Trusted_Connection=yes;Encrypt=no'''

def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn

def close_connection(conn):
    if conn:
        conn.close()

def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select * from Lop"""
        cursor.execute(select_query)
        records = cursor.fetchall()

        print(f"Danh sách các lớp là: ")
        for row in records:
            print("*" * 50)
            print("Mã lớp: ", row[0])
            print("Tên lớp: ", row[1])

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

get_all_class()
def get_all_students():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Lấy danh sách sinh viên (chỉ có mã số, họ tên và mã lớp)
        select_query = """SELECT ID, HoTen, MaLop FROM SinhVien"""
        cursor.execute(select_query)
        records = cursor.fetchall()

        print(f"Danh sách tất cả sinh viên là:")
        print(f"{'Mã số':<5} {'Họ tên':<25} {'Mã lớp':<10}")
        print("=" * 50)
        
        for row in records:
            print(f"{row[0]:<5} {row[1]:<25} {row[2]:<10}")

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

def get_all_students_with_class_name():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Truy vấn có JOIN để lấy cả mã lớp và tên lớp
        select_query = """
        SELECT SinhVien.ID, SinhVien.HoTen, SinhVien.MaLop, Lop.TenLop
        FROM SinhVien
        JOIN Lop ON SinhVien.MaLop = Lop.ID
        """
        cursor.execute(select_query)
        records = cursor.fetchall()

        print(f"Danh sách tất cả sinh viên là:")
        print(f"{'Mã số':<5} {'Họ tên':<25} {'Mã lớp':<10} {'Tên lớp':<10}")
        print("=" * 60)
        
        for row in records:
            print(f"{row[0]:<5} {row[1]:<25} {row[2]:<10} {row[3]:<10}")

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

# Gọi hàm để lấy dữ liệu
get_all_students()
print("\n")
get_all_students_with_class_name()

def get_class_by_id(class_id):  
    try:  
        connection = get_connection()  
        cursor = connection.cursor()  

        # dấu "?" chính là placeholder, điểm đánh dấu vị trí tham số được truyền vào  
        select_query = "select * from Lop where id = ?"  
        # danh sách tham số sẽ truyền vào câu truy vấn  
        params = (class_id,)  
        cursor.execute(select_query, params)  

        record = cursor.fetchone()  

        print(f"Thông tin lớp có id = {class_id} là: ")  
        print("Mã lớp: ", record[0])  
        print("Tên lớp: ", record[1])  

        close_connection(connection)  
    except (Exception, pyodbc.Error) as error:  
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)  

get_class_by_id(1)  

# 1. Tìm sinh viên theo ID
def get_student_by_id(student_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = "SELECT ID, HoTen, MaLop FROM SinhVien WHERE ID = ?"
        params = (student_id,)
        cursor.execute(select_query, params)

        record = cursor.fetchone()
        if record:
            print(f"Thông tin sinh viên có ID {student_id}:")
            print("ID: ", record[0])
            print("Họ tên: ", record[1])
            print("Mã lớp: ", record[2])
        else:
            print(f"Không tìm thấy sinh viên có ID {student_id}")

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

# 2. Hiển thị danh sách sinh viên theo lớp (mã lớp)
def get_students_by_class(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = "SELECT ID, HoTen FROM SinhVien WHERE MaLop = ?"
        params = (class_id,)
        cursor.execute(select_query, params)
        records = cursor.fetchall()

        print(f"Danh sách sinh viên trong lớp {class_id}:")
        print(f"{'ID':<5} {'Họ tên':<25}")
        print("=" * 40)
        
        for row in records:
            print(f"{row[0]:<5} {row[1]:<25}")

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

# 3. Tìm sinh viên theo tên và lớp
def find_student(class_id, student_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """
        SELECT ID, HoTen, MaLop FROM SinhVien
        WHERE MaLop = ? AND HoTen LIKE ?
        """
        params = (class_id, f"%{student_name}%")
        cursor.execute(select_query, params)
        records = cursor.fetchall()

        print(f"Danh sách tất cả sinh viên tên {student_name} ở lớp có mã {class_id}:")
        print(f"{'ID':<5} {'Họ tên':<25} {'Mã lớp':<10}")
        print("=" * 50)

        for row in records:
            print(f"{row[0]:<5} {row[1]:<25} {row[2]:<10}")

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

# Gọi thử các hàm để kiểm tra
print("\n")
get_student_by_id(4)
print("\n")
get_students_by_class(3)
print("\n")
find_student(3, "Trung")