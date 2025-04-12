import tkinter as tk
from math import sin, cos, tan, log, exp, pi

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        master.geometry("500x550")  # Increased window size for better layout

        # Configure background color
        master.configure(bg="#f0f0f0")

        # Display entry
        self.display_var = tk.StringVar()
        self.display = tk.Entry(master, textvariable=self.display_var, width=32, borderwidth=5,
                                 font=('Arial', 18), justify='right', bg="white")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Button styling
        button_style = {'font': ('Arial', 16), 'bg': 'yellow', 'activebackground': 'black'}

        # Define buttons
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        advanced_buttons = [
            'sin', 'cos', 'tan', 'deg',
            'log', 'exp', '√', 'rad',
            'x²', '1/x', '%', 'π'
        ]

        row_index = 1
        col_index = 0

        # Create buttons for basic operations
        for button_text in button_texts:
            button = tk.Button(master, text=button_text, width=5, height=2, command=lambda t=button_text: self.button_click(t), **button_style)
            button.grid(row=row_index, column=col_index)
            col_index += 1
            if col_index > 3:
                col_index = 0
                row_index += 1

        # Create buttons for advanced functions
        col_index = 0
        for button_text in advanced_buttons:
            button = tk.Button(master, text=button_text, width=5, height=2, command=lambda t=button_text: self.button_click(t), **button_style)
            button.grid(row=row_index, column=col_index)
            col_index += 1
            if col_index > 3:
                col_index = 0
                row_index += 1

        # Special buttons
        clear_button = tk.Button(master, text="C", width=5, height=2, command=self.clear_display, **button_style)
        clear_button.grid(row=row_index, column=0)

        backspace_button = tk.Button(master, text="⌫", width=5, height=2, command=self.backspace, **button_style)
        backspace_button.grid(row=row_index, column=1)

    def button_click(self, value):
        current = self.display_var.get()

        if value in ['sin', 'cos', 'tan', 'log', 'exp', '√', 'x²', '1/x']:
            try:
                if value == 'sin':
                    result = str(sin(float(current)))
                elif value == 'cos':
                    result = str(cos(float(current)))
                elif value == 'tan':
                    result = str(tan(float(current)))
                elif value == 'log':
                    result = str(log(float(current)))
                elif value == 'exp':
                    result = str(exp(float(current)))
                elif value == '√':
                    result = str(float(current) ** 0.5)
                elif value == 'x²':
                    result = str(float(current) ** 2)
                elif value == '1/x':
                    if float(current) == 0:
                        result = "Error: Division by zero"
                    else:
                        result = str(1 / float(current))
                self.display_var.set(result)
            except:
                self.display_var.set("Error")

        elif value == 'π':
            self.display_var.set(current + str(pi))

        elif value == 'deg':
            # Implement degree mode conversion logic here
            pass

        elif value == 'rad':
            # Implement radian mode conversion logic here
            pass

        elif value == '=':
            try:
                result = eval(current)
                self.display_var.set(str(result))
            except:
                self.display_var.set("Error")
        else:
            self.display_var.set(current + str(value))

    def clear_display(self):
        self.display_var.set("")

    def backspace(self):
        current = self.display_var.get()
        self.display_var.set(current[:-1])

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()