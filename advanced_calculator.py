# advanced_calculator.py
# 该模块提供了三个功能：计算阶乘、求解方程和计算导数。
#该模块完成了大作业要求：
# 2. 计算阶乘、方程式、求导等（30分）

import math  # 导入数学库，用于计算阶乘
import sympy as sp  # 导入符号计算库，用于求解方程和计算导数

def factorial(n):
    """
    计算 n 的阶乘。

    参数:
    n (int): 需要计算阶乘的非负整数

    返回:
    int: n 的阶乘
    """
    return math.factorial(n)

def solve_equation(equation):
    """
    解方程。

    参数:
    equation (sympy expression): 需要求解的方程

    返回:
    list: 方程的解
    """
    x = sp.symbols('x')  # 定义符号 x
    return sp.solve(equation, x)  # 解方程并返回解

def derivative(equation):
    """
    计算方程的导数。

    参数:
    equation (sympy expression): 需要计算导数的方程

    返回:
    sympy expression: 方程的导数
    """
    x = sp.symbols('x')  # 定义符号 x
    return sp.diff(equation, x)  # 计算并返回导数
