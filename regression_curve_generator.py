import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn.linear_model import LinearRegression

# 设置字体，确保支持中文
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


def create_regression_curve_window():
    # 创建主窗口
    root = tk.Tk()
    root.title("回归曲线生成器")

    # 标签和数值输入
    tk.Label(root, text="输入 x 值（用逗号分隔）:").pack(pady=5)
    entry_labels = tk.Entry(root, width=40)
    entry_labels.pack(pady=5)

    tk.Label(root, text="输入 y 值（用逗号分隔）:").pack(pady=5)
    entry_values = tk.Entry(root, width=40)
    entry_values.pack(pady=5)

    def plot_regression_curve():
        try:
            x_values = list(map(float, entry_labels.get().split(',')))
            y_values = list(map(float, entry_values.get().split(',')))

            if len(x_values) != len(y_values):
                messagebox.showerror("输入错误", "x 和 y 的数量必须相同！")
                return

            x = np.array(x_values).reshape(-1, 1)
            y = np.array(y_values)

            # 使用线性回归模型
            model = LinearRegression()
            model.fit(x, y)
            y_pred = model.predict(x)

            plt.scatter(x, y, color='blue', label='数据点')
            plt.plot(x, y_pred, color='red', label='回归线')
            plt.xlabel("x 值")
            plt.ylabel("y 值")
            plt.title("回归曲线")
            plt.legend()
            plt.tight_layout()
            plt.show()
        except ValueError:
            messagebox.showerror("输入错误", "x 和 y 的值必须是数字！")

    # 按钮
    btn_plot = tk.Button(root, text="生成回归曲线", command=plot_regression_curve)
    btn_plot.pack(pady=20)

    # 主循环
    root.mainloop()
