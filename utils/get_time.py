# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
Created by Wang Han on 29/12/2017 13:23.
E-mail address is hanwang.0501@gmail.com.
Copyright © 2017 Wang Han. SCU. All right Reserved.
"""

from datetime import datetime

chinese_time_dict = {'0': '零', "1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七", "8": "八", "9": "九",
                     "10": "十"}


def get_str_chinese_time():
    def get_str_number(str):
        if str == "零":
            return str
        res = ""
        number = int(str)
        remainder = number // 10
        number = number % 10
        if number == 0 and remainder != 0:
            if remainder != 1:
                res += chinese_time_dict[remainder.__str__()] + "十"
            else:
                res += "十"
        elif number != 0 and remainder == 0:
            res += chinese_time_dict[number.__str__()]
        elif number != 0 and remainder != 0:

            if remainder != 1:
                res += chinese_time_dict[remainder.__str__()] + "十" + chinese_time_dict[number.__str__()]
            else:
                res += "十" + chinese_time_dict[number.__str__()]
        return res

    str = ""
    cur_time = datetime.now()
    cur_year = cur_time.year.__str__()
    cur_month = cur_time.month.__str__()
    cur_day = cur_time.day.__str__()

    # deal year
    for item in cur_year:
        str += chinese_time_dict[item]
    str += "年"

    # deal month
    str += get_str_number(cur_month)
    str += "月"

    # deal day
    str += get_str_number(cur_day)
    str += "日"

    return str


if __name__ == "__main__":
    print(get_str_chinese_time())
