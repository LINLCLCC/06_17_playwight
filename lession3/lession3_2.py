import tkinter as tk
from tkinter import messagebox
<<<<<<< HEAD

def calculate_area():
    try:
        # 取得輸入數值並轉換為浮點數
        top = float(entry_top.get())
        bottom = float(entry_bottom.get())
        height = float(entry_height.get())
        
        # 梯形面積公式: (上底 + 下底) * 高 / 2
        area = (top + bottom) * height / 2
        
        # 更新介面上的公式與面積顯示
        label_formula.config(text=f"計算過程: ({top} + {bottom}) × {height} ÷ 2")
        label_result.config(text=f"梯形面積為: {area:.2f}")
        
    except ValueError:
        messagebox.showerror("錯誤", "請輸入有效的數字！")

# 建立主視窗
root = tk.Tk()
root.title("梯形面積計算器")
root.geometry("400x350")
root.resizable(False, False)

# 1. 顯示公式的區域
label_info = tk.Label(root, text="梯形面積公式：(上底 + 下底) × 高 ÷ 2", font=("Arial", 12, "bold"), fg="blue")
label_info.pack(pady=10)

# 2. 輸入區域介面
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="上底:", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_top = tk.Entry(frame_input, width=15)
entry_top.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="下底:", font=("Arial", 10)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_bottom = tk.Entry(frame_input, width=15)
entry_bottom.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_input, text="高:", font=("Arial", 10)).grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_height = tk.Entry(frame_input, width=15)
entry_height.grid(row=2, column=1, padx=5, pady=5)

# 3. 計算按鈕
btn_calc = tk.Button(root, text="計算面積", command=calculate_area, font=("Arial", 11), bg="#4CAF50", fg="white", width=12)
btn_calc.pack(pady=15)

# 4. 動態顯示計算過程與結果的區域
label_formula = tk.Label(root, text="計算過程: 等待計算...", font=("Arial", 10), fg="gray")
label_formula.pack(pady=5)

label_result = tk.Label(root, text="梯形面積為: --", font=("Arial", 14, "bold"), fg="red")
label_result.pack(pady=5)

# 啟動視窗迴圈
root.mainloop()

      


扝m
=======
from tkinter import font as tkfont


BG_COLOR = "#f4f7fb"
CARD_COLOR = "#ffffff"
PRIMARY_COLOR = "#3b82f6"
PRIMARY_ACTIVE = "#2563eb"
SECONDARY_COLOR = "#e5e7eb"
SECONDARY_ACTIVE = "#d1d5db"
TEXT_COLOR = "#1f2937"
RESULT_COLOR = "#0f766e"
ENTRY_BG = "#f9fafb"


def calculate_area():
    try:
        top = float(top_entry.get().strip())
        bottom = float(bottom_entry.get().strip())
        height = float(height_entry.get().strip())

        if top < 0 or bottom < 0 or height < 0:
            messagebox.showerror("輸入錯誤", "上底、下底與高不能為負數。")
            return

        area = (top + bottom) * height / 2
        result_var.set(f"梯形的面積: {area:.2f} 平方公分")
    except ValueError:
        messagebox.showerror("輸入錯誤", "請輸入有效的數字。")



def clear_fields():
    top_entry.delete(0, tk.END)
    bottom_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_var.set("梯形的面積將顯示在這裡")
    top_entry.focus_set()


root = tk.Tk()
root.title("梯形面積計算器")
root.geometry("460x420")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

heading_font = tkfont.Font(family="Microsoft JhengHei", size=18, weight="bold")
label_font = tkfont.Font(family="Microsoft JhengHei", size=11)
entry_font = tkfont.Font(family="Arial", size=11)
button_font = tkfont.Font(family="Microsoft JhengHei", size=11, weight="bold")
result_font = tkfont.Font(family="Microsoft JhengHei", size=12, weight="bold")

main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.pack(fill="both", expand=True, padx=24, pady=24)

card_frame = tk.Frame(main_frame, bg=CARD_COLOR, bd=0, highlightthickness=0)
card_frame.pack(fill="both", expand=True)

header_label = tk.Label(
    card_frame,
    text="梯形面積計算器",
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    font=heading_font,
)
header_label.pack(pady=(24, 8))

sub_label = tk.Label(
    card_frame,
    text="請輸入上底、下底與高，快速計算梯形面積",
    bg=CARD_COLOR,
    fg="#6b7280",
    font=label_font,
)
sub_label.pack(pady=(0, 20))

form_frame = tk.Frame(card_frame, bg=CARD_COLOR)
form_frame.pack(fill="x", padx=32)


def create_input_row(parent, text):
    frame = tk.Frame(parent, bg=CARD_COLOR)
    frame.pack(fill="x", pady=8)

    label = tk.Label(
        frame,
        text=text,
        bg=CARD_COLOR,
        fg=TEXT_COLOR,
        font=label_font,
        anchor="w",
    )
    label.pack(fill="x", pady=(0, 6))

    entry = tk.Entry(
        frame,
        font=entry_font,
        bg=ENTRY_BG,
        fg=TEXT_COLOR,
        relief="solid",
        bd=1,
        insertbackground=TEXT_COLOR,
        justify="left",
    )
    entry.pack(fill="x", ipady=8)
    return entry


top_entry = create_input_row(form_frame, "請輸入梯形的上底（公分）")
bottom_entry = create_input_row(form_frame, "請輸入梯形的下底（公分）")
height_entry = create_input_row(form_frame, "請輸入梯形的高（公分）")

button_frame = tk.Frame(card_frame, bg=CARD_COLOR)
button_frame.pack(fill="x", padx=32, pady=(20, 12))

calculate_button = tk.Button(
    button_frame,
    text="計算面積",
    command=calculate_area,
    bg=PRIMARY_COLOR,
    fg="white",
    activebackground=PRIMARY_ACTIVE,
    activeforeground="white",
    font=button_font,
    relief="flat",
    bd=0,
    cursor="hand2",
    padx=12,
    pady=10,
)
calculate_button.pack(side="left", expand=True, fill="x", padx=(0, 8))

clear_button = tk.Button(
    button_frame,
    text="清除內容",
    command=clear_fields,
    bg=SECONDARY_COLOR,
    fg=TEXT_COLOR,
    activebackground=SECONDARY_ACTIVE,
    activeforeground=TEXT_COLOR,
    font=button_font,
    relief="flat",
    bd=0,
    cursor="hand2",
    padx=12,
    pady=10,
)
clear_button.pack(side="left", expand=True, fill="x", padx=(8, 0))

result_var = tk.StringVar(value="梯形的面積將顯示在這裡")
result_label = tk.Label(
    card_frame,
    textvariable=result_var,
    bg="#ecfeff",
    fg=RESULT_COLOR,
    font=result_font,
    wraplength=360,
    justify="center",
    padx=16,
    pady=16,
)
result_label.pack(fill="x", padx=32, pady=(8, 24))

top_entry.focus_set()
root.mainloop()
>>>>>>> 0e34d67c82b8b0867dfff63c445995a23ffa92bd
