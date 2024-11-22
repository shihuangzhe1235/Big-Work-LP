import tkinter as tk  
from tkinter import messagebox  

class GomokuGame:  
    def __init__(self, master):  
        self.master = master  
        self.master.title("五子棋小游戏")  
        
        self.board_size = 15  # 棋盘为15x15  
        self.cell_size = 40  # 每个格子的大小  
        self.board = [[0] * self.board_size for _ in range(self.board_size)]  # 0表示空，1表示黑棋，2表示白棋  
        self.current_player = 1  # 1为黑棋，2为白棋  

        self.canvas = tk.Canvas(master, width=self.cell_size * self.board_size, height=self.cell_size * self.board_size, bg='gray')  
        self.canvas.pack()  

        self.draw_board()  
        self.canvas.bind("<Button-1>", self.on_click)  

    def draw_board(self):  
        # 画棋盘  
        for i in range(self.board_size):  
            # 画横线  
            self.canvas.create_line(0, i * self.cell_size, self.board_size * self.cell_size, i * self.cell_size)  
            # 画竖线  
            self.canvas.create_line(i * self.cell_size, 0, i * self.cell_size, self.board_size * self.cell_size)  

    def on_click(self, event):  
        # 获取点击位置  
        x = event.x // self.cell_size  
        y = event.y // self.cell_size  

        if self.board[y][x] == 0:  # 检查该位置是否为空  
            self.board[y][x] = self.current_player  # 在棋盘上放置棋子  
            self.draw_piece(x, y, self.current_player)  # 绘制棋子  

            if self.check_winner(x, y):  # 检查是否获胜  
                winner = "黑棋" if self.current_player == 1 else "白棋"  
                messagebox.showinfo("游戏结束", f"{winner} 获胜！")  
                self.master.quit()  # 结束游戏  

            self.current_player = 3 - self.current_player  # 切换玩家  

    def draw_piece(self, x, y, player):  
        # 绘制棋子  
        if player == 1:  # 黑棋  
            color = "black"  
        else:  # 白棋  
            color = "white"  
        
        # 绘制棋子，白子添加黑边框  
        outline_color = "black" if player == 2 else color  # 白子外加黑边框  
        self.canvas.create_oval(  
            x * self.cell_size + 5,   
            y * self.cell_size + 5,  
            (x + 1) * self.cell_size - 5,  
            (y + 1) * self.cell_size - 5,   
            fill=color,   
            outline=outline_color,   
            width=2  # 边框宽度  
        )  

    def check_winner(self, x, y):  
        # 检查横向、纵向和斜向是否有五颗相同的棋子  
        return (self.check_direction(x, y, 1, 0) or  # 横向  
                self.check_direction(x, y, 0, 1) or  # 纵向  
                self.check_direction(x, y, 1, 1) or  # 正斜向  
                self.check_direction(x, y, 1, -1))   # 反斜向  

    def check_direction(self, x, y, dx, dy):  
        # 检查某个方向上连续棋子的数量  
        count = 1  
        count += self.count_streak(x, y, dx, dy)  # 正方向  
        count += self.count_streak(x, y, -dx, -dy)  # 反方向  
        return count >= 5  

    def count_streak(self, x, y, dx, dy):  
        player = self.board[y][x]  
        count = 0  
        while True:  
            x += dx  
            y += dy  
            if 0 <= x < self.board_size and 0 <= y < self.board_size and self.board[y][x] == player:  
                count += 1  
            else:  
                break  
        return count  

if __name__ == "__main__":  
    root = tk.Tk()  
    game = GomokuGame(root)  
    root.mainloop()