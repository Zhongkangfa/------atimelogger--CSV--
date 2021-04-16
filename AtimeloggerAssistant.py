import csv
import openpyxl
import datetime
import copy

import time


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
        pass

    def simplified(self):

        pass

    def summarizing(self, interval):

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
        self.all_types = set([raw_type[-3] for raw_type in self.raw_types])
            self.group_types = set([raw_type[-4]
                                   for raw_type in self.raw_types if raw_type[-4]])
            self.no_group_types = self.types ^ self.group_types
        pass
