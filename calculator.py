import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title('계산기')

        # 계산기 입력창
        self.entry = tk.Entry(master, width=25, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # 버튼 생성 및 배치
        self.create_button('1', 1, 0)
        self.create_button('2', 1, 1)
        self.create_button('3', 1, 2)
        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('7', 3, 0)
        self.create_button('8', 3, 1)
        self.create_button('9', 3, 2)
        self.create_button('0', 4, 1)
        self.create_button('.', 4, 2)

        self.create_button('+', 1, 3)
        self.create_button('-', 2, 3)
        self.create_button('*', 3, 3)
        self.create_button('/', 4, 3)

        self.create_button('AC', 5, 0)
        self.create_button('=', 5, 1, columnspan=2)
        self.create_button('Quit', 5, 3)

    def create_button(self, text, row, column, columnspan=1):
        button = tk.Button(self.master, text=text, padx=40, pady=20, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan)

    def button_click(self, text):
        if text == 'AC':
            self.entry.delete(0, tk.END)
        elif text == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, '오류')
        elif text == 'Quit':
            self.master.quit()
        else:
            self.entry.insert(tk.END, text)


if __name__ == '__main__':
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
