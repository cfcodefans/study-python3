import numpy as np
from datetime import *
import requests as Req
from lxml import etree
from typing import List
from os import *


# 根据基金代码到 天天基金网拉取数据
# http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=020003&page=10&per=20&sdate=2016-10-01&edate=2017-10-01
# lsjz 历史净值
# code 基金代码
# sdate 开始时间 格式:2016-10-01
# edate 结束时间 格式:2017-10-01
# per 每页多少条
# page 第几页
# 返回 [(日期,净值,增长率)]
def load_raw_data(code: str, sdate: date = None, edate: date = None) -> str:
    if edate is None:
        edate = datetime.now().date()

    if sdate is None:
        sdate = date(edate.year - 3, edate.month, edate.day)

    print(code, sdate, edate)

    url: str = f"http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code={code}&page=1&per=3000&sdate={sdate}&edate={edate}"
    print("开始加载数据", url)

    resp: Req.Response = Req.get(url, headers={
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4"})

    result_str: str = resp.content.decode("utf-8")
    #    print(result_str)
    #    print(result_str.index("<table"), result_str.index("table>"))
    data_str: str = result_str[result_str.index("<table"):result_str.index("table>") + len("table>")]
    # print(data_str)
    return data_str


def _if(flag: bool, a, b):
    if flag:
        return a
    return b


def try_float(s: str, _default: float = 0.0) -> float:
    try:
        return float(s)
    except ValueError:
        return _default


def parse_raw_data(data_str: str) -> np.ndarray:
    el: etree._Element = etree.HTML(data_str)
    trList: List[etree._Element] = el.xpath("//tbody/tr")
    data: np.ndarray = np.array([[td for td in tr.xpath("./td/text()")[:4]] for tr in trList])
    data = np.array(
        [[datetime.strptime(row[0], '%Y-%m-%d'), try_float(row[1]), try_float(row[2]), try_float(row[3][:-1])] for row
         in data])
    data = data[::-1]
    return data


def get_fund_data(code: str, sdate: date = None, edate: date = None) -> np.ndarray:
    folder_path: str = f"c:\\temp\\fund"
    if not path.exists(folder_path):
        mkdir(folder_path)

    file_path: str = f"c:\\temp\\fund\\{code}.csv"
    if not path.exists(file_path):
        print(f"found no data file at:\n\t{file_path}")
        now: date = datetime.now()
        start: date = date(now.year - 5, now.month, now.day)
        loaded: np.ndarray = parse_raw_data(load_raw_data(code, start))
        print(loaded[0:3])
        loaded = np.array([np.append([row[0].strftime("%Y-%m-%d")], row[1:]) for row in loaded])
        print(loaded[0:3])
        np.savetxt(file_path, loaded, delimiter=",", fmt=["%s", "%.4f", "%.4f", "%.4f"])
        print(f"load and save data to:\n\t{file_path}")

    if edate is None:
        edate = datetime.now().date()

    if sdate is None:
        sdate = date(edate.year - 3, edate.month, edate.day)

    start: str = sdate.strftime("%Y-%m-%d")
    end: str = edate.strftime("%Y-%m-%d")

    data: np.ndarray = np.loadtxt(file_path, delimiter=",", dtype={
        "names": ("date", "price", "value", "change"),
        "formats": ("S10", "f", "f", "f")})

    data_in_span: List = np.array(
        [list(row) for row in data if start <= str(row[0].decode('utf-8')) <= end])
    data = np.array([np.append(np.array(datetime.strptime(row[0].decode('utf-8'), "%Y-%m-%d")), row[1:]) for row in data_in_span])
    return data
