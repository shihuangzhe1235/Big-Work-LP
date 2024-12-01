import tkinter as tk
from tkinter import ttk
from sympy import *
import sympy

# 初始化符号
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

# 定义求解函数
def oneEquation_Solve_systems_of_linear_equations(equation):
    return solve(equation, x)

def twoEquation_Solve_systems_of_linear_equations(equation):
    return solve(equation, [x, y])

def threeEquation_Solve_systems_of_linear_equations(equation):
    return solve(equation, [x, y, z])

def oneEquation_Solve_systems_of_nonlinear_equations(equation):
    return sympy.nonlinsolve(equation, x)

def twoEquation_Solve_systems_of_nonlinear_equations(equation):
    return sympy.nonlinsolve(equation, [x, y])

def threeEquation_Solve_systems_of_nonlinear_equations(equation):
    return sympy.nonlinsolve(equation, [x, y, z])

def Solve_differential_equations(equation):
    f = symbols('f', cls=Function)
    return dsolve(equation, f(x))
#例子 1.Eq(f(x).diff(x, x) - 2*f(x).diff(x) + f(x), sin(x))     2.Eq(f(x).diff(x, x) - 3*f(x).diff(x) + 2*f(x), exp(-x))        3.Eq(f(x).diff(x, x) - 4*f(x), 0)
# 创建 GUI 应用程序的类
class EquationSolverApp:
    def __init__(self, root):
        self.root = root
        root.title("方程求解器")

        # 输入方程的标签
        self.label = tk.Label(root, text="输入方程（每个方程一行）：")
        self.label.pack()

        # 方程输入框（多行）
        self.equation_input = tk.Text(root, height=10, width=50)
        self.equation_input.pack()

        # 选择方程类型
        self.equation_type = ttk.Combobox(root, values=["线性方程", "非线性方程", "微分方程"])
        self.equation_type.set("选择方程类型")
        self.equation_type.pack()

        # 解决按钮
        self.solve_button = tk.Button(root, text="求解", command=self.solve_equations)
        self.solve_button.pack()

        # 显示结果的区域
        self.result_label = tk.Label(root, text="结果：")
        self.result_label.pack()
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack()

    def solve_equations(self):
        # 获取输入方程和选定的类型
        equations_str = self.equation_input.get("1.0", tk.END).strip().splitlines()
        equations = [sympify(eq.strip()) for eq in equations_str if eq.strip()]  # 排除空行
        eq_type = self.equation_type.get()

        # 根据所选类型求解方程
        try:
            if eq_type == "线性方程":
                if len(equations) == 1:
                    result = oneEquation_Solve_systems_of_linear_equations(equations[0])
                elif len(equations) == 2:
                    result = twoEquation_Solve_systems_of_linear_equations(equations)
                elif len(equations) == 3:
                    result = threeEquation_Solve_systems_of_linear_equations(equations)
                else:
                    result = "请提供1到3个线性方程。"

            elif eq_type == "非线性方程":
                if len(equations) == 1:
                    result = oneEquation_Solve_systems_of_nonlinear_equations(equations[0])
                elif len(equations) == 2:
                    result = twoEquation_Solve_systems_of_nonlinear_equations(equations)
                elif len(equations) == 3:
                    result = threeEquation_Solve_systems_of_nonlinear_equations(equations)
                else:
                    result = "请提供1到3个非线性方程。"

            elif eq_type == "微分方程":
                if len(equations) == 1:
                    result = Solve_differential_equations(equations[0])
                else:
                    result = "请提供一个微分方程。"
            else:
                result = "请选择方程类型。"

        except Exception as e:
            result = f"求解出错：{e}"

        # 显示结果
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, str(result))


# 主程序
if __name__ == "__main__":
    root = tk.Tk()
    app = EquationSolverApp(root)
    root.mainloop()