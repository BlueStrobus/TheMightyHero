import tkinter as tk

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("계산기")
        self.geometry("250x350")

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        result_frame = tk.Frame(self)
        result_frame.pack(pady=10)

        result_entry = tk.Entry(result_frame, textvariable=self.result_var, font=("Arial", 24), bd=10, justify="right")
        result_entry.pack()

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        for i in range(9):
            btn = tk.Button(button_frame, text=str(i + 1), font=("Arial", 14), command=lambda i=i: self.add_number(i + 1))
            btn.grid(row=(2 - i // 3), column=(i % 3), padx=5, pady=5)

        zero_btn = tk.Button(button_frame, text="0", font=("Arial", 14), command=lambda: self.add_number(0))
        zero_btn.grid(row=3, column=0, padx=5, pady=5)

        clear_btn = tk.Button(button_frame, text="C", font=("Arial", 14), command=self.clear)
        clear_btn.grid(row=3, column=1, padx=5, pady=5)

        equal_btn = tk.Button(button_frame, text="=", font=("Arial", 14), command=self.calculate)
        equal_btn.grid(row=3, column=2, padx=5, pady=5)

        operators = ["+", "-", "*", "/"]
        for i, operator in enumerate(operators):
            btn = tk.Button(button_frame, text=operator, font=("Arial", 14), command=lambda op=operator: self.add_operator(op))
            btn.grid(row=i, column=3, padx=5, pady=5)

    def add_number(self, number):
        current_result = self.result_var.get()
        if current_result == "0" or current_result == "오류":
            self.result_var.set(str(number))
        else:
            self.result_var.set(current_result + str(number))

    def add_operator(self, operator):
        current_result = self.result_var.get()
        if current_result[-1] not in ["+", "-", "*", "/"]:
            self.result_var.set(current_result + operator)

    def clear(self):
        self.result_var.set("0")

    def calculate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("오류")

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()

    asdfasfasf
