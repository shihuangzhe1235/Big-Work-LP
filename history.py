#该模块完成了大作业要求：
# 4.创意功能(10分）,实现了一个简单的历史记录功能，用于记录和显示用户的计算



# 用于存储历史操作的列表
history = []

def log_history(operation):
    """
    记录一项操作到历史记录中。

    参数:
    operation (str): 需要记录的操作描述
    """
    history.append(operation)  # 将操作添加到历史记录中

def show_history():
    """
    显示历史记录。

    返回:
    list: 当前的历史记录列表
    """
    return history  # 返回历史记录
