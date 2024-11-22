import tkinter as tk
import random
import os

class Game2048:
    def __init__(self, master):
        self.master = master
        self.master.title("2048 Game")
        self.center_window(400, 450)  # 设置窗口居中
        # 初始化游戏板，4x4的矩阵，初始值为0
        self.board = [[0] * 4 for _ in range(4)]
        self.score = 0  # 初始化分数
        self.create_widgets()
        self.reset_game()
        # 绑定键盘事件
        self.master.bind("<Key>", self.key_handler)

    def center_window(self, width, height):
        # 获取屏幕宽度和高度
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        # 计算窗口左上角的位置
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.master.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        # 创建一个顶部框架用于放置按钮和记分牌
        top_frame = tk.Frame(self.master)
        top_frame.pack(fill=tk.X, pady=10)

        # 创建排行榜按钮
        leaderboard_button = tk.Button(top_frame, text="Leaderboard", command=self.show_leaderboard)
        leaderboard_button.pack(side=tk.RIGHT, padx=10)
        
        # 创建重启按钮
        restart_button = tk.Button(top_frame, text="Restart", command=self.reset_game)
        restart_button.pack(side=tk.RIGHT, padx=10)

        # 创建记分牌
        self.score_label = tk.Label(top_frame, text=f"Score: {self.score}", font=("Helvetica", 12))
        self.score_label.pack(side=tk.RIGHT, padx=10)

        # 创建一个400x400的画布
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="white")
        self.canvas.pack(pady=0)  # 调整pady参数
        self.draw_grid()

    def draw_grid(self):
        # 定义不同数字对应的颜色
        colors = {
            0: "lightgray",
            2: "lightyellow",
            4: "lightgoldenrod",
            8: "orange",
            16: "darkorange",
            32: "tomato",
            64: "red",
            128: "yellow",
            256: "gold",
            512: "lightgreen",
            1024: "green",
            2048: "darkgreen"
        }
        
        # 绘制4x4的网格
        for i in range(4):
            for j in range(4):
                x0, y0 = i * 100, j * 100
                x1, y1 = x0 + 100, y0 + 100
                value = self.board[j][i]
                color = colors.get(value, "black")  # 获取对应颜色，默认黑色
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
                if value != 0:
                    # 在非零的格子中间绘制数字
                    self.canvas.create_text(x0 + 50, y0 + 50, text=str(value), font=("Helvetica", 24), fill="black")

    def reset_game(self):
        # 重置游戏板和分数
        self.board = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.update_score()
        # 添加两个初始的随机方块
        self.add_new_tile()
        self.add_new_tile()
        self.update_ui()

    def add_new_tile(self):
        # 找到所有空的格子
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        if empty_cells:
            # 随机选择一个空格子，并放入2或4
            i, j = random.choice(empty_cells)
            self.board[i][j] = 2 if random.random() < 0.9 else 4

    def update_ui(self):
        # 更新UI，重新绘制网格
        self.canvas.delete("all")
        self.draw_grid()

    def update_score(self):
        # 更新记分牌
        self.score_label.config(text=f"Score: {self.score}")

    def key_handler(self, event):
        # 处理键盘事件
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            if self.move(event.keysym):
                # 如果移动成功，添加一个新的随机方块
                self.add_new_tile()
                self.update_ui()
                # 检查游戏是否结束或胜利
                if self.check_win():
                    self.win()
                elif self.check_game_over():
                    self.game_over()

    def move(self, direction):
        # 滑动并合并行或列
        def slide(row):
            new_row = [i for i in row if i != 0]
            for i in range(len(new_row) - 1):
                if new_row[i] == new_row[i + 1]:
                    new_row[i] *= 2
                    self.score += new_row[i]  # 更新分数
                    new_row[i + 1] = 0
            new_row = [i for i in new_row if i != 0]
            return new_row + [0] * (4 - len(new_row))

        moved = False
        if direction == "Up":
            for j in range(4):
                col = [self.board[i][j] for i in range(4)]
                new_col = slide(col)
                for i in range(4):
                    if self.board[i][j] != new_col[i]:
                        moved = True
                    self.board[i][j] = new_col[i]
        elif direction == "Down":
            for j in range(4):
                col = [self.board[i][j] for i in range(4)]
                new_col = slide(col[::-1])[::-1]
                for i in range(4):
                    if self.board[i][j] != new_col[i]:
                        moved = True
                    self.board[i][j] = new_col[i]
        elif direction == "Left":
            for i in range(4):
                new_row = slide(self.board[i])
                if self.board[i] != new_row:
                    moved = True
                self.board[i] = new_row
        elif direction == "Right":
            for i in range(4):
                new_row = slide(self.board[i][::-1])[::-1]
                if self.board[i] != new_row:
                    moved = True
                self.board[i] = new_row
        if moved:
            self.update_score()  # 更新分数
        return moved

    def check_win(self):
        # 检查是否达到2048
        for row in self.board:
            if 2048 in row:
                return True
        return False

    def check_game_over(self):
        # 检查游戏是否结束
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    return False
                if i < 3 and self.board[i][j] == self.board[i + 1][j]:
                    return False
                if j < 3 and self.board[i][j] == self.board[i][j + 1]:
                    return False
        return True

    def game_over(self):
        # 显示游戏结束信息
        self.canvas.create_text(200, 200, text="Game Over", font=("Helvetica", 36), fill="red")
        self.save_score()  # 保存分数到文件

    def win(self):
        # 显示胜利信息
        self.canvas.create_text(200, 200, text="You win!", font=("Helvetica", 36), fill="green")
        self.save_score()  # 保存分数到文件

    def save_score(self):
        # 保存当前分数到文件
        with open("scores.txt", "a") as file:
            file.write(f"{self.score}\n")

    def show_leaderboard(self):
        # 读取分数并显示排行榜
        if os.path.exists("scores.txt"):
            with open("scores.txt", "r") as file:
                scores = [int(line.strip()) for line in file.readlines()]
            scores.sort(reverse=True)
            top_scores = scores[:10]
        else:
            top_scores = []

        # 创建一个新的窗口显示排行榜
        leaderboard_window = tk.Toplevel(self.master)
        leaderboard_window.title("Leaderboard")
        leaderboard_window.geometry("200x250")
        tk.Label(leaderboard_window, text="Top 10 Scores", font=("Helvetica", 16)).pack()
        for idx, score in enumerate(top_scores, 1):
            tk.Label(leaderboard_window, text=f"{idx}. {score}", font=("Helvetica", 14)).pack()

if __name__ == "__main__":
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()
