# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
Created by Wang Han on 27/12/2017 18:53.
E-mail address is hanwang.0501@gmail.com.
Copyright © 2017 Wang Han. SCU. All right Reserved.
"""
from app.models import Comment
from app import db
import math


def add_comment(text):
    comment = Comment(text)
    db.session.add(comment)
    db.session.commit()


def delete_comment(comment_id):
    comment = select_comment(comment_id)
    db.session.delete(comment)
    db.session.commit()


def select_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()
    return comment


def update_comment(comment_id, new_text):
    comment = select_comment(comment_id)
    comment.text = new_text
    db.session.commit()


# get total number of comment
def get_comment_count():
    return Comment.query.count()


def get_all_comments():
    comments = Comment.query.all()
    return comments


# get comment by offset from 0 to count(*)-1
def get_comment_by_offset(offset):
    return Comment.query.offset(offset).first()


# get pagination
def get_page(length, page, pagesize=5):
    p_len = int(math.ceil(length / pagesize))
    p_list = range(1, p_len+1)
    start = 0
    end = pagesize
    if page and page > 1:
        start = (page-1) * pagesize
        end = page * pagesize
        if start > length:
            start = length - pagesize
            end = length
        elif end > length:
            end = length

    if page == 0:
        start = length - pagesize
        end = length
    return p_list, start, end
