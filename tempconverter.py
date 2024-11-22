from tkinter import *
from converters import * #导入conventr
class ScaleConverter:
	
	def __init__(self, units_from, units_to, factor):
		self.units_from = units_from
		self.units_to = units_to
		self.factor = factor
	
	def description(self):
		return 'Convert ' + self.units_from + ' to ' + self.units_to
 
	def convert(self, value):
		return value * self.factor
 
class ScaleAndOffsetConverter(ScaleConverter):
	
	def __init__(self, units_from, units_to, factor, offset):
		ScaleConverter.__init__(self, units_from, units_to, factor)
		self.offset = offset
		
	def convert(self, value):
		return value * self.factor + self.offset
class App:
 
    def __init__(self,master):
        self.t_conv = ScaleAndOffsetConverter('C','F',1.8,32)
        #创建一个Frame实例
        frame = Frame(master)
        #界面中放置一个frame
        frame.pack()
        #在frame中第1行第1列放置一个Label标签 deg C 摄氏度
        Label(frame,text='deg C').grid(row=0,column=0)
        
        self.c_var =DoubleVar()
        #在frame中第1行第2列放置一个Entry文本框
        Entry(frame,textvariable=self.c_var).grid(row=0,column=1)
        #在frame中第2行第1列放置一个Label标签，用来输入要转换的 deg C 摄氏温度
        Label(frame,text='deg F').grid(row=1,column=0)
        
        #在frame中第2行第2列放置一个Label标签，用来显示转换结果 deg F 华氏温度
        self.result_var = DoubleVar()
        
        #Label(frame,textvariable=self.result_var).grid(row=1,column=1)
        Label(frame,textvariable=self.result_var).grid(row=1,column=1)
        
        #在frame中创建一个button实例
        button = Button(frame, text='Convert', command=self.convert)
        
        #在frame中第3行放置这个button
        button.grid(row=2,columnspan=2)
        
    def convert(self):
        #获取Entry文本框的值self.c_var
        c = self.c_var.get()
        #设置转换结果Label标签 deg F 华氏温度的值
        self.result_var.set(self.t_conv.convert(c))
        
 
 
root = Tk()
root.wm_title('Temp Converter')
app = App(root)
root.mainloop()

