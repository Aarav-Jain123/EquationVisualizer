import tkinter as tk
import tkinter.messagebox as messagebox
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, symbols, solve

class LinearGrapher:
    def __init__(self, root):
        self.root = root
        self.root.title("Algebraic Equation Visualizer")
        
        # UI Elements
        self.label = tk.Label(root, text="Enter equations (one per line):\nExample: 2*x + 3")
        self.label.pack(pady=10)

        self.text_input = tk.Text(root, height=5, width=30)
        self.text_input.pack(pady=5)

        self.plot_button = tk.Button(root, text="Plot 2D Graph", command=self.plot_2d)
        self.plot_button.pack(pady=10)

    def parse_equation(self, eq_str):
        try:
            x = symbols('x')
            expr = sympify(eq_str)
            return expr
        except Exception as e:
            raise ValueError(f"Invalid Equation: {eq_str}")

    def plot_2d(self):
        lines = self.text_input.get("1.0", tk.END).strip().split('\n')
        if not lines or lines[0] == '':
            messagebox.showwarning("Input Error", "Please enter at least one equation.")
            return

        plt.figure(figsize=(8, 6))
        x_vals = np.linspace(-10, 10, 400)

        try:
            for i, line in enumerate(lines):
                expr = self.parse_equation(line)
                
                import sympy
                f = sympy.lambdify(symbols('x'), expr, 'numpy')
                y_vals = f(x_vals)
                
                plt.plot(x_vals, y_vals, label=f"y = {line}")

            plt.axhline(0, color='black', linewidth=1)
            plt.axvline(0, color='black', linewidth=1)
            plt.grid(True, linestyle='--')
            plt.legend()
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title("Linear Equation in One Variable Comparison")
            plt.show()
            
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = LinearGrapher(root)
    root.mainloop()