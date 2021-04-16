from tkinter import *
from tkinter import filedialog
from AtimeloggerAssistant import AtimeloggerAssistant


class MyApp(Tk):

    def __init__(self):
        super().__init__()

        self.setupUI()

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
        self.url_line_edit = Entry(self, bg='white', width=45)
        self.browse_button = Button(
            self, text='浏览', width=8, command=self.select_csv_file)
        self.collating_button = Button(
            self, text='整理报告', width=8, command=self.collating)
        self.exit_button = Button(
            self, text='退出', width=8, command=self.destroy)

    def layout(self):
        self.select_label.grid(row=0, column=0)
        self.url_line_edit.grid(row=0, column=1)
        self.browse_button.grid(row=0, column=2)
        self.collating_button.grid(row=1, column=2)
        self.exit_button.grid(row=2, column=2)
        pass

    def select_csv_file(self):
        filename = filedialog.askopenfilename(
            title='选择Excel文件',
            filetypes=[
                ('csv', '*.csv')]
        )
        self.url_line_edit.insert(INSERT, filename)
        pass

    def collating(self):
        # 创建对象
        assistant = AtimeloggerAssistant()
        # 添加report
        assistant.add_report()
        # 加工精简
        assistant.simplified()
        # 按天汇总
        assistant.summarizing('day')
        # 按周汇总
        assistant.summarizing('week')
        # 按月汇总
        assistant.summarizing('month')

        pass
