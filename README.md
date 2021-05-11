### 相比遗留的代码（Legacy Code）

#### 有了简陋的GUI

![face](https://github.com/Zhongkangfa/deal_with_atimelogger_export_CSV/blob/master/img/GUI.png)

能够让用户选择指定文件，处理后还能指定导出的位置。

#### 拆分多个文件，逻辑更清晰

| 文件名                  | 说明                                                         |
| ----------------------- | ------------------------------------------------------------ |
| ThinterWin.py           | 用Thinter编写的窗口对象                                      |
| AtimeloggerAssistant.py | 抽象为一个助理，负责处理从atimelogger APP导出的CSV文件。处理流程请看他work()方法。 |
| Activity.py             | Core！代表时间记录中活动类别。进一步抽象封装——将核心业务逻辑封装起来。方便外层调用。 |



#### 增添了断言（assert）

为了减少不必要的争议，做了如下断言

- 结束时间不能小于开始时间；
- 一次活动间隔不能超过24小时；
- 活动类别不支持重名；



### 代码说明（note）

#### 如何添加选择文件的对话框的交互窗口？

```python
from tkinter import filedialog

self.csv_path = filedialog.askopenfilename(
            title='请选择csv文件',
            filetypes=[
                ('csv文件', '*.csv')]
        )
```

#### 如何修改Worksheet的名称(title)？

```python
ws.title = "365 Days"
```

#### 如何给列表（list）去重？

```python
my_list = [1,1,1]
my_list = list(set(my_list))
```
#### 如何将时间字符串转换为datetime数据类型？

```python
import datetime
datetime_str = '2019/5/5 21:59:33'
datetime.datetime.strptime(datetime_str, "%Y/%m/%d %H:%M:%S")
```

#### 要访问的字典不存在指定的key时，如何添加默认值并在此基础上运算？

```python
container = dict()
container["max"] = container.get("max", 100) + 50
```

