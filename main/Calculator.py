# 시작하세요import tkinter as tk

import tkinter as tk
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        
        # 입력창 생성
        self.entry = tk.Entry(master, width=35, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # 버튼 생성
        button_1 = self.create_button(1, 1, "1")
        button_2 = self.create_button(1, 2, "2")
        button_3 = self.create_button(1, 3, "3")
        button_4 = self.create_button(2, 1, "4")
        button_5 = self.create_button(2, 2, "5")
        button_6 = self.create_button(2, 3, "6")
        button_7 = self.create_button(3, 1, "7")
        button_8 = self.create_button(3, 2, "8")
        button_9 = self.create_button(3, 3, "9")
        button_0 = self.create_button(4, 2, "0")
        button_add = self.create_button(1, 4, "+")
        button_subtract = self.create_button(2, 4, "-")
        button_multiply = self.create_button(3, 4, "*")
        button_divide = self.create_button(4, 4, "/")
        button_clear = self.create_button(4, 1, "C")
        button_equal = self.create_button(4, 3, "=")
        
        self.buttons = [button_1, button_2, button_3, button_4, button_5, button_6,
                        button_7, button_8, button_9, button_0, button_add, button_subtract,
                        button_multiply, button_divide, button_clear, button_equal]
        
        # 계산기 상태 초기화
        self.clear()
        
        # 키보드 입력을 처리할 수 있도록 바인딩
        self.master.bind("<Key>", lambda event: self.button_click(event.char))
        
    def create_button(self, row, column, text=None):
        button = tk.Button(self.master, padx=40, pady=20, text=text,
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=column)
        return button
    
    def button_click(self, text):
        if text == "C":
            self.clear()
        elif text == "=":
            self.calculate()
        elif text.isdigit():
            self.entry.insert(tk.END, text)
    def handle_keypress(self, event):
        key = event.keysym
        if key.isdigit():
            self.button_click(key)

        self.master.bind("<Key>", self.handle_keypress)
            
    def clear(self):
        self.entry.delete(0, tk.END)
        
    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except:
            self.clear()
            self.entry.insert(0, "Error")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()

# 키보드로 숫자 입력 시 2번 입력되는 오류가 있다 