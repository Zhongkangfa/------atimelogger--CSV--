from tkinter import Tk, Label, Entry, Button, INSERT, messagebox,DISABLED
from tkinter import filedialog
from AtimeloggerAssistant import AtimeloggerAssistant


class MyApp(Tk):

    def __init__(self):
        super().__init__()

        self.setupUI()
        self.csv_path = ''

    def setupUI(self):
        self.title("选择atimelogger report")
        self.win_center()
        self.resizable(0, 0)

        self.create_widget()
        self.layout()

    def win_center(self):
        ww = 470
        wh = 100
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw-ww) / 2
        y = (sh-wh) / 2
        self.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

    def create_widget(self):
        self.select_label = Label(self, text='请选择文件:')
        self.url_label = Label(self, bg='white', width=45)
        self.browse_button = Button(
            self, text='浏览', width=8, command=self.select_csv_file)
        self.collating_button = Button(
            self, text='整理报告', width=8, command=self.collating)
        self.exit_button = Button(
            self, text='退出', width=8, command=self.destroy)

    def layout(self):
        self.select_label.grid(row=0, column=0)
        self.url_label.grid(row=0, column=1)
        self.browse_button.grid(row=0, column=2)
        self.collating_button.grid(row=1, column=2)
        self.exit_button.grid(row=2, column=2)
        pass

    def select_csv_file(self):
        self.csv_path = filedialog.askopenfilename(
            title='选择csv文件',
            filetypes=[
                ('csv文件', '*.csv')]
        )
        print(self.csv_path)
        self.url_label['text'] = "..." + self.csv_path[-30:]
        pass

    def save_file(self):
        file_name = filedialog.asksaveasfilename(
            title='Python tkinter', filetypes=[("EXCEL 文件", ".xlsx")])
        return file_name

    def collating(self):
        # 创建对象
        assistant = AtimeloggerAssistant()
        # 添加report
        assistant.add_report(self.csv_path)
        # 整理
        assistant.work()
        # 汇总
        assistant.summarizing()
        messagebox.showinfo('提示','数据处理成功！准备保存并关闭软件。')
        # 保存并退出
        file_name = self.save_file()
        if not file_name: 
            print("已取消！")
            return
        else:
            assistant.save(file_name)
            self.destroy()
        pass
