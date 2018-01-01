# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
Created by Wang Han on 28/12/2017 23:57.
E-mail address is hanwang.0501@gmail.com.
Copyright © 2017 Wang Han. SCU. All right Reserved.
"""

from app.comment_helper import add_comment


"""
Read comments from file and insert them into database.
"""
with open('./语言内容汇总.txt', 'r', encoding='utf-8') as file:
    line = file.readline().strip('\n')
    while line:
        add_comment(line)
        line = file.readline().strip('\n')
print("success")
