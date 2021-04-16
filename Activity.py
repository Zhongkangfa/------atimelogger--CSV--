import datetime


class Activity:
    def __init__(self, name, own_intervals):
        self.name = name
        self.intervals = own_intervals
        self.days = {}
        self.weeks = {}
        self.months = {}
        self._scan()
        # self.test()
        # print(self.intervals)
        pass

    def test(self):
        print(self.months)

    def total_by_day(self, day):
        return self.days[day]

    def total_by_week(self, week):
        return self.weeks[week]

    def total_by_month(self, month):
        return self.months[month]

    def _scan(self):
        for interval in self.intervals:
            # 第一步：判断开始时间和结束时间是不是同一天
            # ['形象', '00:32:35', '2019/5/5 21:59:33', '2019/5/5 22:32:08', '']
            start_time = datetime.datetime.strptime(
                interval[2], "%Y/%m/%d %H:%M:%S")
            over_time = datetime.datetime.strptime(
                interval[3], "%Y/%m/%d %H:%M:%S")

            start_date = start_time.date()
            over_date = over_time.date()
            
            if start_date == over_date:
                duration = over_time - start_time
                self.days[start_date] = self.days.get(
                    start_date, datetime.timedelta()) + duration
                self.weeks[str(start_date.year)+"-"+str(start_date.weekday())] = self.weeks.get(
                    str(start_date.year)+"-"+str(start_date.weekday()), datetime.timedelta()) + duration
                self.months[str(start_date.year)+"-"+str(start_date.month)] = self.months.get(
                    str(start_date.year)+"-"+str(start_date.month), datetime.timedelta()) + duration
            else:
                datetime_zero_point = datetime.datetime(
                    over_time.year, over_time.month, over_time.day)

                # 0点之前
                duration = datetime_zero_point - start_time
                self.days[start_date] = self.days.get(start_date, datetime.timedelta()) + duration
                self.weeks[str(start_date.year)+"-"+str(start_date.weekday())] = self.weeks.get(
                    str(start_date.year)+"-"+str(start_date.weekday()), datetime.timedelta()) + duration
                self.months[str(start_date.year)+"-"+str(start_date.month)] = self.months.get(
                    str(start_date.year)+"-"+str(start_date.month), datetime.timedelta()) + duration

                # 0点之后
                duration = over_time - datetime_zero_point
                self.days[over_date] = self.days.get(
                    over_date, datetime.timedelta()) + duration
                self.weeks[str(over_date.year)+"-"+str(over_date.weekday())] = self.weeks.get(
                    str(over_date.year)+"-"+str(over_date.weekday()), datetime.timedelta()) + duration
                self.months[str(over_date.year)+"-"+str(over_date.month)] = self.months.get(
                    str(over_date.year)+"-"+str(over_date.month), datetime.timedelta()) + duration

        pass
