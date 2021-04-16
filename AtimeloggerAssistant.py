import csv
import openpyxl
import datetime
import copy
from Activity import *


class AtimeloggerAssistant:
    def __init__(self):
        self.file = None
        self.wb = openpyxl.Workbook()
        self.create_sheet()

        self.days_dict = {}
        self.raw_intervals = []
        self.raw_types = []
        self.types = set()
        self.group_types = set()
        self.no_group_types = set()
        self.activitys = []
        self.all_life = []
        pass

    def create_sheet(self):
        self.ws_simplified_data = self.wb.active
        self.ws_days = self.wb.create_sheet("365 Days")
        self.ws_weeks = self.wb.create_sheet("52 Weeks")
        self.ws_months = self.wb.create_sheet("12 Months")

    def add_report(self, csv_path):
        self.file_path = csv_path
        self.separate()
        self.get_activity_type_info()
        self.create_activitys()
        pass


    def summarizing(self):
        table_header = list(self.no_group_types)
        table_header.insert(0, "")
        self.ws_days.append(table_header)
        self.all_life = set([datetime.datetime.strptime(
                interval[2], "%Y/%m/%d %H:%M:%S").date() for interval in self.raw_intervals])

        # 制作第一张表单
        for life_date in sorted(list(self.all_life)):
            row_for_ws_days = [str(life_date)]
            # row_for_ws_weeks = [str(life_date.year)+"-"+str(life_date.weekday())]
            # row_for_ws_months = [str(life_date.year)+"-"+str(life_date.month)]
            for activity in self.activitys:
                counted_activity_time = round(activity.days.get(life_date, datetime.timedelta()).seconds/3600, 2)
                row_for_ws_days.append(counted_activity_time)
            self.ws_days.append(row_for_ws_days)

        # 保存
        self.wb.save("after.xlsx")
        print("保存成功！")

            
        pass

    def separate(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            read = csv.reader(f)
            read.__next__()

            # 收集原始的intervals，待进一步处理
            for row in read:
                if row:
                    self.raw_intervals.append(row[-5:])
                elif not row:
                    break

            read.__next__()

            # 收集原始的types
            for row in read:
                self.raw_types.append(row)
        pass

    def get_activity_type_info(self):
        """我的程序暂不支持重名活动类别"""
        # all_types = group + activity
        self.all_types = set([raw_type[-3] for raw_type in self.raw_types])
        # group_types = group
        self.group_types = set([raw_type[-4]
                                for raw_type in self.raw_types if raw_type[-4]])
        # no_group_types = activity
        self.no_group_types = self.all_types ^ self.group_types
        
        pass

    def create_activitys(self):
        for activity_name in self.no_group_types:
            own_intervals = [interval for interval in self.raw_intervals if interval[0] == activity_name]
            # ['形象', '00:32:35', '2019/5/5 21:59:33', '2019/5/5 22:32:08', '']
            self.activitys.append(Activity(activity_name, own_intervals))
        pass