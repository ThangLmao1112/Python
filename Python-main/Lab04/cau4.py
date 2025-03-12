import tkinter as tk
from tkinter import messagebox

# Danh sách lưu công việc
tasks_list = []
counter = 1  # Đếm số công việc


# Hàm kiểm tra nhập trống
def input_error():
    if enter_task_field.get().strip() == "":
        messagebox.showerror("Lỗi", "Vui lòng nhập công việc!")
        return True
    return False


# Hàm xóa nội dung ô nhập công việc
def clear_task_field():
    enter_task_field.delete(0, tk.END)


# Hàm xóa nội dung ô nhập số thứ tự
def clear_task_number_field():
    task_number_field.delete(0, tk.END)


# Hàm thêm công việc vào danh sách
def insert_task():
    global counter

    if input_error():
        return

    task = enter_task_field.get().strip()
    tasks_list.append(task)

    # Cập nhật danh sách công việc
    update_task_list()

    # Xóa ô nhập
    clear_task_field()


# Hàm cập nhật danh sách công việc
def update_task_list():
    task_area.delete(1.0, tk.END)
    for idx, task in enumerate(tasks_list, 1):
        task_area.insert(tk.END, f"{idx}. {task}\n")


# Hàm xóa công việc theo số thứ tự
def delete_task():
    global counter

    if not tasks_list:
        messagebox.showerror("Lỗi", "Danh sách công việc trống!")
        return

    task_no = task_number_field.get().strip()

    if not task_no.isdigit():
        messagebox.showerror("Lỗi", "Vui lòng nhập số thứ tự hợp lệ!")
        return

    task_no = int(task_no)

    if task_no < 1 or task_no > len(tasks_list):
        messagebox.showerror("Lỗi", "Số thứ tự không tồn tại!")
        return

    # Xóa công việc
    tasks_list.pop(task_no - 1)
    clear_task_number_field()

    # Cập nhật danh sách công việc
    update_task_list()


# Hàm thoát ứng dụng
def exit_app():
    root.destroy()


# ----------------- Giao diện -----------------
root = tk.Tk()
root.title("Quản Lý Công Việc")
root.geometry("400x450")
root.configure(bg="#f4f4f4")

# Tiêu đề
title_label = tk.Label(
    root, text="Quản Lý Công Việc", font=("Arial", 16, "bold"), bg="#f4f4f4", fg="#333"
)
title_label.pack(pady=10)

# Nhập công việc
frame_input = tk.Frame(root, bg="#f4f4f4")
frame_input.pack(pady=5)

tk.Label(frame_input, text="Nhập công việc:", font=("Arial", 12), bg="#f4f4f4").pack(
    side=tk.LEFT, padx=5
)
enter_task_field = tk.Entry(frame_input, width=30, font=("Arial", 12))
enter_task_field.pack(side=tk.LEFT, padx=5)

# Nút thêm công việc
add_button = tk.Button(
    root,
    text="Thêm",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=insert_task,
)
add_button.pack(pady=10)

# Khu vực hiển thị danh sách công việc
task_area = tk.Text(
    root,
    height=10,
    width=45,
    font=("Arial", 12),
    bg="white",
    relief="solid",
    wrap="word",
)
task_area.pack(pady=5)

# Nhập số thứ tự công việc cần xóa
frame_delete = tk.Frame(root, bg="#f4f4f4")
frame_delete.pack(pady=5)

tk.Label(frame_delete, text="Xóa công việc số:", font=("Arial", 12), bg="#f4f4f4").pack(
    side=tk.LEFT, padx=5
)
task_number_field = tk.Entry(frame_delete, width=5, font=("Arial", 12))
task_number_field.pack(side=tk.LEFT, padx=5)

# Nút xóa công việc
delete_button = tk.Button(
    root,
    text="Xóa",
    font=("Arial", 12, "bold"),
    bg="#f44336",
    fg="white",
    command=delete_task,
)
delete_button.pack(pady=10)

# Nút thoát ứng dụng
exit_button = tk.Button(
    root,
    text="Thoát",
    font=("Arial", 12, "bold"),
    bg="#555",
    fg="white",
    command=exit_app,
)
exit_button.pack(pady=10)

# Chạy chương trình
root.mainloop()
