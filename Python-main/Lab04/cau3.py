from tkinter import *

# Biến toàn cục để lưu biểu thức
expression = ""


def press(num):
    global expression
    expression += str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except:
        equation.set("Error")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


# Giao diện GUI
root = Tk()
root.title("Máy Tính")
root.geometry("350x400")
root.configure(bg="#F0F0F0")

equation = StringVar()

# Ô hiển thị biểu thức
entry = Entry(
    root,
    textvariable=equation,
    font=("Arial", 18),
    bd=10,
    relief=RIDGE,
    justify="right",
)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

# Thiết lập các nút bấm
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3),
]

for text, row, col in buttons:
    color = "#5B9BD5" if text.isdigit() or text == "." else "#FFA500"
    Button(
        root,
        text=text,
        font=("Arial", 14, "bold"),
        fg="white",
        bg=color,
        width=7,
        height=2,
        bd=3,
        relief=RAISED,
        command=lambda t=text: press(t) if t != "=" else equalpress(),
    ).grid(row=row, column=col, padx=5, pady=5)

# Nút Clear
Button(
    root,
    text="C",
    font=("Arial", 14, "bold"),
    fg="white",
    bg="#FF4C4C",
    width=7,
    height=2,
    bd=3,
    relief=RAISED,
    command=clear,
).grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="we")

root.mainloop()
