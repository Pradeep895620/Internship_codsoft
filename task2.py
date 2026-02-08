
import tkinter as tk  
from tkinter import messagebox  

class Calculator:  
    def __init__(self, root):  
        self.root = root  
        self.root.title("Simple Calculator")  
        self.root.geometry("300x400")  

        self.current_input = ""  
        self.result = 0.0  
        self.last_operation = ""  

        # Display Field  
        self.display_var = tk.StringVar(value="0")  
        self.display_field = tk.Entry(  
            root, textvariable=self.display_var, font=("Arial", 24),  
            justify="right", state="readonly"  
        )  
        self.display_field.pack(side="top", fill="x", padx=10, pady=10)  

        # Button Panel  
        self.button_panel = tk.Frame(root)  
        self.button_panel.pack(expand=True, fill="both", padx=5, pady=5)  

        button_labels = [  
            "7", "8", "9", "/",  
            "4", "5", "6", "*",  
            "1", "2", "3", "-",  
            "0", ".", "=", "+",  
            "C", "%"  
        ]  

        # Create buttons using a grid (5 rows, 4 columns)  
        row, col = 0, 0  
        for label in button_labels:  
            btn = tk.Button(  
                self.button_panel, text=label, font=("Arial", 18),  
                command=lambda l=label: self.on_click(l)  
            )  
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)  
            
            col += 1  
            if col > 3:  
                col = 0  
                row += 1  

        # Configure grid weights so buttons resize  
        for i in range(5):  
            self.button_panel.rowconfigure(i, weight=1)  
        for i in range(4):  
            self.button_panel.columnconfigure(i, weight=1)  

    def on_click(self, command):  
        if command.isdigit() or command == ".":  
            self.current_input += command  
            self.display_var.set(self.current_input)  
        
        elif command == "C":  
            self.current_input = ""  
            self.result = 0.0  
            self.last_operation = ""  
            self.display_var.set("0")  
        
        elif command == "=":  
            self.calculate_result()  
            self.last_operation = ""  
            
        else:  # Operator buttons  
            if self.current_input:  
                if self.last_operation:  
                    self.calculate_result()  
                else:  
                    self.result = float(self.current_input)  
            
            self.last_operation = command  
            self.current_input = ""  

    def calculate_result(self):  
        if not self.current_input and self.last_operation != "=":  
            return  

        try:  
            second_operand = float(self.current_input) if self.current_input else self.result
            
            if self.last_operation == "+":  
                self.result += second_operand  
            elif self.last_operation == "-":  
                self.result -= second_operand  
            elif self.last_operation == "*":  
                self.result *= second_operand  
            elif self.last_operation == "/":  
                if second_operand != 0:  
                    self.result /= second_operand  
                else:  
                    self.display_var.set("Error: Div by 0")  
                    self.current_input = ""  
                    self.result = 0  
                    return  
            elif self.last_operation == "%":  
                self.result %= second_operand  

            self.display_var.set(str(self.result))  
            self.current_input = str(self.result)  
            
        except ValueError:  
            pass  

if __name__ == "__main__":  
    root = tk.Tk()  
    app = Calculator(root)  
    root.mainloop()  
