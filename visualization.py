#该模块完成了大作业要求：
# 3. 画图功能，柱状图，饼状图，回归曲线等（30分）



import matplotlib.pyplot as plt  # 导入绘图模块
import numpy as np  # 导入数值计算模块

def plot_bar_chart():
    """
    绘制柱状图，用户输入类别和对应值。
    """
    print("——— 柱状图输入 ———")
    # 获取用户输入的类别和对应值
    labels = input("请输入类别（如：产品名称，用逗号分隔，例如：产品A,产品B,产品C,产品D）：").split(',')
    values = list(map(float, input("请输入对应的值（如：销售额，用逗号分隔，例如：100,150,200,50）：").split(',')))

    # 绘制柱状图
    plt.bar(labels, values)
    plt.title('柱状图')  # 设置标题
    plt.xlabel('类别')  # 设置X轴标签
    plt.ylabel('值')  # 设置Y轴标签
    plt.show()  # 显示图表

def plot_pie_chart():
    """
    绘制饼状图，用户输入类别和对应占比。
    """
    print("——— 饼状图输入 ———")
    # 获取用户输入的类别和对应占比
    labels = input("请输入类别（如：市场名称，用逗号分隔，例如：市场A,市场B,市场C,市场D）：").split(',')
    sizes = list(map(float, input("请输入对应的占比（如：市场份额，用逗号分隔，例如：40,30,20,10）：").split(',')))

    # 绘制饼状图
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')  # 绘制饼图并显示百分比
    plt.title('饼状图')  # 设置标题
    plt.axis('equal')  # 使饼图为圆形
    plt.show()  # 显示图表

def plot_regression_curve():
    """
    绘制回归曲线，用户输入自变量和因变量数据。
    """
    print("——— 回归曲线输入 ———")
    # 获取用户输入的自变量和因变量数据
    x = list(map(float, input("请输入自变量数据（如：时间或其他变量，用逗号分隔，例如：1,2,3,4,5）：").split(',')))
    y = list(map(float, input("请输入因变量数据（如：对应值，用逗号分隔，例如：2.2,2.8,3.6,4.5,5.1）：").split(',')))

    # 计算线性回归系数
    coefficients = np.polyfit(x, y, 1)
    polynomial = np.poly1d(coefficients)  # 创建多项式对象

    # 绘制散点图和回归曲线
    plt.scatter(x, y, color='blue', label='数据点')  # 绘制数据点
    plt.plot(x, polynomial(x), color='red', label='回归曲线')  # 绘制回归曲线
    plt.title('回归曲线示例')  # 设置标题
    plt.xlabel('自变量')  # 设置X轴标签
    plt.ylabel('因变量')  # 设置Y轴标签
    plt.legend()  # 显示图例
    plt.show()  # 显示图表


########################################
# 柱状图 (plot_bar_chart):
#
# 用户输入类别和对应的值，绘制柱状图。
# 使用 plt.bar() 函数绘制。
# 饼状图 (plot_pie_chart):
#
# 用户输入类别和对应的占比，绘制饼状图。
# 使用 plt.pie() 函数绘制，并显示百分比。
# 回归曲线 (plot_regression_curve):
#
# 用户输入自变量和因变量数据，计算线性回归并绘制回归曲线。
# 使用 np.polyfit() 计算回归系数，并使用 plt.scatter() 和 plt.plot() 绘制数据点和回归曲线。