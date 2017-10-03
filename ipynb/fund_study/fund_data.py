import numpy as np
from datetime import *
import requests as Req
from lxml import etree


def get_fund_data(code: str, sdate: date = None, edate: date = None) -> np.ndarray:
    if edate is None:
        edate = datetime.now().date()

    if sdate is None:
        sdate = date(edate.year - 3, edate.month, edate.day)

    print(code, sdate, edate)

    url: str = f"http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code={code}&page=1&per=3000&sdate={sdate}&edate={edate}"
    print("loading data from", url)

    resp: Req.Response = Req.get(url, headers={
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4"})

    result_str: str = resp.content.decode("utf-8")
    #    print(result_str)
    #    print(result_str.index("<table"), result_str.index("table>"))
    data_str: str = result_str[result_str.index("<table"):result_str.index("table>") + len("table>")]

    el: etree._Element = etree.HTML(data_str)
    el.xpath("/table/tbody/tr")

    return None


get_fund_data('020003', sdate=None)
