import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置字体，确保支持中文
rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
def plot_bar_chart():
    # 创建主窗口
    root = tk.Toplevel()
    root.title("柱状图生成器")

    # 标签和数值输入
    tk.Label(root, text="输入标签（用逗号分隔）:").pack(pady=5)
    entry_labels = tk.Entry(root, width=40)
    entry_labels.pack(pady=5)

    tk.Label(root, text="输入数值（用逗号分隔）:").pack(pady=5)
    entry_values = tk.Entry(root, width=40)
    entry_values.pack(pady=5)

    # 独立绘制柱状图的逻辑
    def generate_bar_chart():
        try:
            labels = entry_labels.get().split(',')
            values = list(map(float, entry_values.get().split(',')))

            if len(labels) != len(values):
                messagebox.showerror("输入错误", "标签和数值的数量必须相同！")
                return

            plt.bar(labels, values, color='skyblue')
            plt.xlabel("标签")
            plt.ylabel("数值")
            plt.title("柱状图")
            plt.tight_layout()
            plt.show()
        except ValueError:
            messagebox.showerror("输入错误", "数值必须是数字！")

    # 按钮绑定到绘制函数
    btn_plot = tk.Button(root, text="生成柱状图", command=generate_bar_chart)
    btn_plot.pack(pady=20)

    # 子窗口的主循环
    root.mainloop()