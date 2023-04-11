#계산기 용
import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("계산기")

        # 계산기에 사용되는 버튼과 연산자
        self.buttons = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', 'C', '+']

        # 계산기 화면
        self.display = tk.Entry(master, width=25, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, pady=5)

        # 버튼 생성
        self.create_buttons()

        # 초기화 버튼에 이벤트 바인딩
        self.master.bind('<Return>', self.calculate)
        
        # 삭제 버튼에 이벤트 바인딩
        self.master.bind('<Delete>', lambda event: self.display.delete(0, tk.END))

    def create_buttons(self):
        # 버튼 생성 및 이벤트 바인딩
        row, col = 1, 0
        for button in self.buttons:
            if button == 'C':
                tk.Button(self.master, text=button, width=7, height=2, command=self.clear).grid(row=row, column=col)
            else:
                tk.Button(self.master, text=button, width=7, height=2, command=lambda x=button: self.display.insert(tk.END, x)).grid(row=row, column=col)

            col += 1
            if col > 3:
                col = 0
                row += 1

        # 계산 버튼 생성
        tk.Button(self.master, text='=', width=7, height=2, command=self.calculate).grid(row=5, column=3)

    def clear(self):
        # 화면 초기화
        self.display.delete(0, tk.END)

    def calculate(self, event=None):
        # 계산 수행
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
