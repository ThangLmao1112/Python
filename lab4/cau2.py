import tkinter as tk
from tkinter import messagebox

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Đăng nhập")
root.geometry("400x250")

# Căn giữa cửa sổ
root.eval("tk::PlaceWindow . center")

# Biến lưu dữ liệu nhập vào
name_var = tk.StringVar()
passw_var = tk.StringVar()
show_password_var = tk.BooleanVar() 

def submit():
    name = name_var.get()
    password = passw_var.get()
    if name == "admin" and password == "123":
        messagebox.showinfo("Thông báo", "Đăng nhập thành công!")
    else:
        messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng!")
    name_var.set("")
    passw_var.set("")

def toggle_password():
    if show_password_var.get():
        passw_entry.config(show="")
    else:
        passw_entry.config(show="*")

tk.Label(root, text="Tên đăng nhập:", font=("Arial", 12)).grid(
    row=0, column=0, padx=10, pady=10, sticky="w"
)
name_entry = tk.Entry(root, textvariable=name_var, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Mật khẩu:", font=("Arial", 12)).grid(
    row=1, column=0, padx=10, pady=10, sticky="w"
)
passw_entry = tk.Entry(root, textvariable=passw_var, font=("Arial", 12), show="*")
passw_entry.grid(row=1, column=1, padx=10, pady=10)

show_pass_cb = tk.Checkbutton(
    root, text="Hiện mật khẩu", variable=show_password_var, command=toggle_password
)
show_pass_cb.grid(row=2, column=1, sticky="w", padx=10)

sub_btn = tk.Button(
    root,
    text="Đăng nhập",
    font=("Arial", 12, "bold"),
    command=submit,
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
)
sub_btn.grid(row=3, column=1, pady=20)

root.mainloop()
