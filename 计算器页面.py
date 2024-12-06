import tkinter as tk
from sympy import *
import subprocess
import re
import math
import matplotlib.pyplot as plt
import numpy as np

from Games.mathquiz import MathQuizApp
from Games.gamewuzi import GomokuGame
from Games.game2048 import Game2048
from bar_chart import plot_bar_chart
from pie_chart import create_pie_chart_window
from regression_curve_generator import create_regression_curve_window
from Solve_equations import EquationSolverApp
root = tk.Tk()
root.title('计算器')
# 界面大小
root.geometry('500x500')

root.attributes("-alpha", 0.9)
#root["background"] = "#ffffff"
font = ('Arial', 20)
font_16 = ('Arial', 16)

result_num = tk.StringVar()
#result_num.set('0')

tk.Label(root,
         textvariable=result_num, font=font, height=2,
         width=25, anchor=tk.SE
         ).grid(row=1, column=1, columnspan=5)

button_pow = tk.Button(root, text='^', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_log = tk.Button(root, text='log', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_comma = tk.Button(root, text=',', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_lb = tk.Button(root, text='(', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_rb = tk.Button(root, text=')', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_pow.grid(row=2, column=1, padx=4, pady=2)
button_log.grid(row=2, column=2, padx=4, pady=2)
button_comma.grid(row=2, column=3, padx=4, pady=2)
button_lb.grid(row=2, column=4, padx=4, pady=2)
button_rb.grid(row=2, column=5, padx=4, pady=2)

button_sqrt = tk.Button(root, text='√', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_clear = tk.Button(root, text='C', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_back = tk.Button(root, text='←', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_division = tk.Button(root, text='/', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_mult = tk.Button(root, text='*', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_sqrt.grid(row=3, column=1, padx=4, pady=2)
button_clear.grid(row=3, column=2, padx=4, pady=2)
button_back.grid(row=3, column=3, padx=4, pady=2)
button_division.grid(row=3, column=4, padx=4, pady=2)
button_mult.grid(row=3, column=5, padx=4, pady=2)
button_factorial = tk.Button(root, text='!', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_seven = tk.Button(root, text='7', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_eight = tk.Button(root, text='8', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_nine = tk.Button(root, text='9', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_sub = tk.Button(root, text='-', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_game14 = tk.Button(root, text='启动Game14', width=12, font=('Arial', 16), relief=tk.FLAT, bg='#b1b2b2')
button_factorial.grid(row=4, column=1, padx=4, pady=2)
button_seven.grid(row=4, column=2, padx=4, pady=2)
button_eight.grid(row=4, column=3, padx=4, pady=2)
button_nine.grid(row=4, column=4, padx=4, pady=2)
button_sub.grid(row=4, column=5, padx=4, pady=2)
button_game14.grid(row=10, column=1, padx=4, pady=2, columnspan=2)
button_diff = tk.Button(root, text='求导', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_four = tk.Button(root, text='4', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_five = tk.Button(root, text='5', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_six = tk.Button(root, text='6', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_add = tk.Button(root, text='+', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_diff.grid(row=5, column=1, padx=4, pady=2)
button_four.grid(row=5, column=2, padx=4, pady=2)
button_five.grid(row=5, column=3, padx=4, pady=2)
button_six.grid(row=5, column=4, padx=4, pady=2)
button_add.grid(row=5, column=5, padx=4, pady=2)

button_pi = tk.Button(root, text='π', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_one = tk.Button(root, text='1', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_two = tk.Button(root, text='2', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_three = tk.Button(root, text='3', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_mod = tk.Button(root, text='%', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_pi.grid(row=6, column=1, padx=4, pady=2)
button_one.grid(row=6, column=2, padx=4, pady=2)
button_two.grid(row=6, column=3, padx=4, pady=2)
button_three.grid(row=6, column=4, padx=4, pady=2)
button_mod.grid(row=6, column=5, padx=4, pady=2)

button_e = tk.Button(root, text='e', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_zero = tk.Button(root, text='0', width=12, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_dot = tk.Button(root, text='.', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
button_equal = tk.Button(root, text='=', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_e.grid(row=7, column=1, padx=4, pady=2)
button_zero.grid(row=7, column=2, padx=4, pady=2, columnspan=2)
button_dot.grid(row=7, column=4, padx=4, pady=2)
button_equal.grid(row=7, column=5, padx=4, pady=2)

button_bar = tk.Button(root, text='柱状图', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_pie = tk.Button(root, text='饼状图', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_equation = tk.Button(root, text='求方程', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_huigui = tk.Button(root, text='回归线', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_uknum = tk.Button(root, text='x', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_equation.grid(row=8, column=1, padx=4, pady=2)
button_bar.grid(row=8, column=2, padx=4, pady=2)
button_pie.grid(row=8, column=3, padx=4, pady=2)
button_huigui.grid(row=8, column=4, padx=4, pady=2)
button_uknum.grid(row=8, column=5, padx=4, pady=2)


# # 添加"Start Computer"按钮 特色功能2048游戏
button_2048 = tk.Button(root, text='2048游戏', width=12, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
button_2048.grid(row=9, column=1, padx=4, pady=2, columnspan=2)

# # 创建跳转到问答游戏的按钮
button_quiz = tk.Button(root, text='问答游戏', width=12, font=('Arial', 16), relief=tk.FLAT, bg='#b1b2b2')
button_quiz.grid(row=9, column=3, padx=4, pady=2, columnspan=2)

# 创建跳转到五子棋游戏的按钮
button_gomoku = tk.Button(root, text='五子棋', width=5, font=('Arial', 16), relief=tk.FLAT, bg='#b1b2b2')
button_gomoku.grid(row=9, column=5, padx=4, pady=2)


#############点击事件##############
"""为求方程绑定一个求方程页面跳转"""
def open_game14():
    try:
        file_path = r"Games/Pac-Man/Game14.py"
        subprocess.run(["python", file_path], check=True)
        root.destroy()  # 启动后关闭当前窗口
    except Exception as e:
        print(f"启动 Game14.py 时出现错误: {e}")
def open_solve_equations():
    eq=tk.Toplevel(root)
    app = EquationSolverApp(eq)
def click_button(x):
    print('x:\t',x)
    result_num.set(result_num.get() + x)
#计算表达式
def calculation():
    opt_str = result_num.get()
    if "!" in opt_str:
        opt_str = factorial_replace(opt_str)

    opt_str = opt_str.replace('e', str(math.e))
    opt_str = opt_str.replace('^', '**')
    opt_str = opt_str.replace('√', 'math.sqrt')
    opt_str = opt_str.replace('π', str(math.pi))
    # 匹配对数表达式并替换
    pattern = r"log\(([^,]+),\s*([^)]+)\)"
    opt_str = re.sub(pattern, lambda m: f"math.log({m.group(2)})/math.log({m.group(1)})", opt_str)
    # 计算最终结果
    try:
        result = eval(opt_str)
        result_num.set(str(result))
    except Exception as e:
        result_num.set("表达式错误！")
        print(f"Error evaluating expression: {e}")

#清屏操作
def clear():
    result_num.set("")

#退格操作
def back():
    str = result_num.get()
    str = str[:len(str) - 1]
    result_num.set(str)

#求导数
def derivative():
    x = symbols('x')  # 定义符号 x
    tmp = result_num.get().replace("^", "**")
    tmp = tmp.replace('√', 'math.sqrt')
    tmp = tmp.replace('π', str(math.pi))
    tmp = tmp.replace('e', str(math.e))
    new_str = str(diff(tmp, x))
    print(new_str)
    result_num.set(new_str.replace("**", "^"))

"""为2048绑定一个页面跳转"""
def open_2048_game():
    game_2048_window = tk.Toplevel(root)
    game = Game2048(game_2048_window)

button_2048.config(command=open_2048_game)

"""为数字游戏绑定一个页面跳转"""
def open_math_quiz():
    quiz_window = tk.Toplevel(root)
    app = MathQuizApp(quiz_window)

button_quiz.config(command=open_math_quiz)

"""为五子棋绑定一个页面跳转"""
def open_gomoku_game():
    gomoku_window = tk.Toplevel(root)
    game = GomokuGame(gomoku_window)

button_gomoku.config(command=open_gomoku_game)

#计算阶乘
def factorial_replace(opt_str):
    obj = re.compile(r"(?P<data>\d+)!")
    matches = obj.findall(opt_str)
    for i in matches:
        print(i)
        re_result = factorial(int(i))
        print(re_result)
        opt_str = opt_str.replace(i + "!", str(re_result))
    return opt_str

def open_bar_chart_page():
    # 这里可以进行一些数据准备等操作，假设绘图函数需要的数据已在对应文件中定义好或者后续可以补充传入合适的数据
    plot_bar_chart()
def open_pie_chart_page():
    create_pie_chart_window()
def open_regression_curve_page():
    create_regression_curve_window()
#######点击按钮显示在屏幕上#########
button_one.config(command=lambda:click_button('1'))
button_two.config(command=lambda:click_button('2'))
button_three.config(command=lambda:click_button('3'))
button_four.config(command=lambda:click_button('4'))
button_five.config(command=lambda:click_button('5'))
button_six.config(command=lambda:click_button('6'))
button_seven.config(command=lambda:click_button('7'))
button_eight.config(command=lambda:click_button('8'))
button_nine.config(command=lambda:click_button('9'))
button_zero.config(command=lambda:click_button('0'))
button_add.config(command=lambda:click_button('+'))
button_sub.config(command=lambda:click_button('-'))
button_mult.config(command=lambda:click_button('*'))
button_division.config(command=lambda:click_button('/'))
button_mod.config(command=lambda:click_button('%'))
button_factorial.config(command=lambda:click_button('!'))
button_sqrt.config(command=lambda:click_button('√('))
button_pow.config(command=lambda:click_button('^'))
button_log.config(command=lambda:click_button('log('))
button_comma.config(command=lambda:click_button(','))
button_dot.config(command=lambda:click_button('.'))
button_lb.config(command=lambda:click_button('('))
button_rb.config(command=lambda:click_button(')'))
button_pi.config(command=lambda:click_button('π'))
button_e.config(command=lambda:click_button('e'))
button_uknum.config(command=lambda:click_button('x'))
button_bar.config(command=open_bar_chart_page)
button_pie.config(command=open_pie_chart_page)
button_huigui.config(command=open_regression_curve_page)
##########给按钮绑定功能###########
button_equal.config(command=calculation)
button_clear.config(command=clear)
button_back.config(command=back)
button_diff.config(command=derivative)
button_equation.config(command=open_solve_equations)
button_game14.config(command=open_game14)
root.mainloop()