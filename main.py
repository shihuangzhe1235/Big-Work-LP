# main.py
# 这段代码是整个计算器项目的主程序，整合了基本计算、高级计算、绘图功能和历史记录.


from calculator import add, subtract, multiply, divide, power, logarithm, exponent
from advanced_calculator import factorial, solve_equation, derivative
from visualization import plot_bar_chart, plot_pie_chart, plot_regression_curve
from history import log_history, show_history


def basic_calculator():
    """基本计算器功能，支持加、减、乘、除、幂、对数和指数运算"""
    print("选择操作:")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    print("5. 幂运算")
    print("6. 对数运算")
    print("7. 指数运算")

    choice = input("输入你的选择（1/2/3/4/5/6/7）:")

    if choice in ['1', '2', '3', '4', '5']:
        # 对于加、减、乘、除和幂运算，要求用户输入两个数字
        num1 = float(input("输入第一个数字: "))
        num2 = float(input("输入第二个数字: "))

        if choice == '1':
            result = add(num1, num2)
            operation = f"{num1} + {num2} = {result}"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = f"{num1} - {num2} = {result}"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = f"{num1} * {num2} = {result}"
        elif choice == '4':
            result = divide(num1, num2)
            operation = f"{num1} / {num2} = {result}"
        elif choice == '5':
            result = power(num1, num2)
            operation = f"{num1} 的 {num2} 次方 = {result}"

    elif choice == '6':
        # 对数运算，要求用户输入要计算的值和底
        num = float(input("输入要计算对数的值: "))
        base = float(input("输入对数的底: "))
        result = logarithm(num, base)
        operation = f"log_{base}({num}) = {result}"

    elif choice == '7':
        # 指数运算，要求用户输入指数值
        exp_num = float(input("输入要计算指数的值: "))
        result = exponent(exp_num)
        operation = f"e^{exp_num} = {result}"

    else:
        operation = "无效输入"  # 处理无效选择

    print(operation)  # 输出结果
    log_history(operation)  # 记录操作历史
    print("历史记录:", show_history())  # 显示历史记录


def advanced_calculator():
    """高级计算器功能，支持阶乘、解方程和求导"""
    print("选择高级功能:")
    print("1. 计算阶乘")
    print("2. 解方程")
    print("3. 求导")

    choice = input("输入你的选择（1/2/3）:")

    if choice == '1':
        # 计算阶乘
        num = int(input("输入一个整数计算阶乘: "))
        print(f"{num}! = {factorial(num)}")
    elif choice == '2':
        # 解方程
        eq = input("输入方程式（例如 x**2 - 4）: ")
        result = solve_equation(eq)
        print(f"方程 {eq} 的解: {result}")
    elif choice == '3':
        # 求导
        eq = input("输入需要求导的表达式（例如 x**2 + 3*x + 2）: ")
        print(f"{eq} 的导数是: {derivative(eq)}")
    else:
        print("无效输入")  # 处理无效选择


def main():
    """主程序循环，提供用户选择并调用相应功能"""
    while True:
        print("\n欢迎使用计算器！")
        print("1. 基本计算器")
        print("2. 高级计算器")
        print("3. 绘图功能")
        print("4. 退出")

        choice = input("输入你的选择（1/2/3/4）:")

        if choice == '1':
            basic_calculator()  # 调用基本计算器功能
        elif choice == '2':
            advanced_calculator()  # 调用高级计算器功能
        elif choice == '3':
            # 调用绘图功能
            plot_bar_chart()
            plot_pie_chart()
            plot_regression_curve()
        elif choice == '4':
            break  # 退出程序
        else:
            print("无效输入")  # 处理无效选择


if __name__ == "__main__":
    main()  # 运行主程序
