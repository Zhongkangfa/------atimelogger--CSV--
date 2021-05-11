import datetime


class Activity:
    def __init__(self, name, own_intervals):
        self.name = name
        self.intervals = own_intervals
        self.days = {}
        self.weeks = {}
        self.months = {}
        self.zero_delta = datetime.timedelta()
        self.__scan()
        pass

    def total(self, time_unit):
        pass

    def total_by_day(self, day):
        seconds = self.days.get(day, self.zero_delta).total_seconds()
        hours = round(seconds/3600, 2)
        return hours

    def total_by_week(self, week):
        seconds = self.weeks.get(week, self.zero_delta).total_seconds()
        hours = round(seconds/3600, 2)
        return hours

    def total_by_month(self, month):
        seconds = self.months.get(month, self.zero_delta).total_seconds()
        hours = round(seconds/3600, 2)
        return hours

    def __scan(self):
        """
        逐条处理时间记录（interval），一次性汇总到各个容器（dict）
        满足当前该程序最基本的业务需求。
        """
        for interval in self.intervals:
            # 第一步：判断开始时间和结束时间是不是同一天
            # ['形象', '00:32:35', '2019/5/5 21:59:33', '2019/5/5 22:32:08', '']
            start_time = datetime.datetime.strptime(
                interval[2], "%Y/%m/%d %H:%M:%S")
            over_time = datetime.datetime.strptime(
                interval[3], "%Y/%m/%d %H:%M:%S")
            
            #进行断言
            assert over_time >= start_time, " 逻辑错误：结束时间小于开始时间, 该条时间记录是："+str(interval)
            assert (over_time - start_time).seconds <= 86400, " 提示：该条时间记录时长超过24小时，为了减少不必要的错误和误差，程序终止："+str(interval)

            start_date = start_time.date()
            over_date = over_time.date()

            start_week = start_date.strftime("%Y-%W")
            over_week = over_date.strftime("%Y-%W")

            start_month = start_date.strftime("%Y-%m")
            over_month = over_date.strftime("%Y-%m")

            if start_date == over_date:
                duration = over_time - start_time
                self.days[start_date] = self.days.get(
                    start_date, self.zero_delta) + duration
                self.weeks[start_week] = self.weeks.get(
                    start_week, self.zero_delta) + duration
                self.months[start_month] = self.months.get(
                    start_month, self.zero_delta) + duration
            else:
                datetime_zero_point = datetime.datetime(
                    over_time.year, over_time.month, over_time.day)

                # 0点之前
                duration = datetime_zero_point - start_time
                self.days[start_date] = self.days.get(
                    start_date, self.zero_delta) + duration
                self.weeks[start_week] = self.weeks.get(
                    start_week, self.zero_delta) + duration
                self.months[start_month] = self.months.get(
                    start_month, self.zero_delta) + duration

                # 0点之后
                duration = over_time - datetime_zero_point
                self.days[over_date] = self.days.get(
                    over_date, self.zero_delta) + duration
                self.weeks[over_week] = self.weeks.get(
                    over_week, self.zero_delta) + duration
                self.months[over_month] = self.months.get(
                    over_month, self.zero_delta) + duration
        pass
