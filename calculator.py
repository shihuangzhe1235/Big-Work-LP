#该模块完成了大作业要求：
# 1.加减乘除、幂计算功能（30分）;
# 4.部分创意功能(10分）新增了对数运算和指数运算

import math

def add(x, y):
    """返回 x 和 y 的和"""
    return x + y

def subtract(x, y):
    """返回 x 和 y 的差"""
    return x - y

def multiply(x, y):
    """返回 x 和 y 的积"""
    return x * y

def divide(x, y):
    """返回 x 和 y 的商，处理除数为零的情况"""
    if y == 0:
        return "除数不能为零"
    return x / y


def power(x, y):
    """返回 x 的 y 次方"""
    return x ** y

#######################################################
##接下来是创意拓展功能，为计算器添加了对数、指数运算相应的函数

#创意功能 1

def logarithm(x, base):
    """
    返回 x 的以 base 为底的对数。
    如果 base 不合法，返回错误信息。
    """
    if x <= 0:
        return "对数的值必须大于零"
    if base <= 1:
        return "对数的底必须大于 1"
    return math.log(x, base)

def exponent(x):
    """返回 e 的 x 次方"""
    return math.exp(x)
