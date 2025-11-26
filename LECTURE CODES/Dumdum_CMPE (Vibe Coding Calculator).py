import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")
        root.resizable(False, False)
        root.geometry("400x550")

        self.screen_var = tk.StringVar()
        self.expr = ""
        self.last_operator = ""
        self.last_number = ""
        self.memory = []

        # Display
        self.entry = tk.Entry(root, textvar=self.screen_var, font="Arial 24", bd=5, relief="sunken", justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, pady=10, padx=10)

        # Buttons
        buttons = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['0','.','=','+'],
            ['C','M']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for btn in row:
                b = tk.Button(frame, text=btn, font="Arial 20", relief="raised", bd=3)
                b.pack(side="left", expand=True, fill="both")
                b.bind("<Button-1>", self.click)

    def click(self, event):
        text = event.widget.cget("text")

        if text == "=":
            try:
                if self.last_operator and self.last_number:
                    # Repeat last operation if user presses '=' again
                    self.expr += self.last_operator + self.last_number
                result = str(eval(self.expr))
                if len(result) > 16:
                    result = f"{float(result):.6E}"
                self.screen_var.set(result)

                # Save last operation
                tokens = self.expr.rstrip('0123456789.').split()
                if any(op in self.expr for op in '+-*/'):
                    # Find last operator and number
                    for op in '+-*/':
                        if op in self.expr:
                            self.last_operator = op
                    self.last_number = self.expr.split(self.last_operator)[-1]
                self.expr = result
                self.memory.append(result)
            except:
                self.screen_var.set("Error")
                self.expr = ""
                self.last_operator = ""
                self.last_number = ""
        elif text == "C":
            self.expr = ""
            self.last_operator = ""
            self.last_number = ""
            self.screen_var.set("")
        elif text == "M":
            if self.memory:
                self.expr += self.memory[-1]
                self.screen_var.set(self.expr)
        else:
            self.expr += text
            self.screen_var.set(self.expr)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
