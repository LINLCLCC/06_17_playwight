import tkinter as tk
from tkinter import messagebox

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