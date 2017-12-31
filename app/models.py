# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
Created by Wang Han on 27/12/2017 15:39.
E-mail address is hanwang.0501@gmail.com.
Copyright © 2017 Wang Han. SCU. All right Reserved.
"""

from app import db


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256), nullable=False)

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return "<Comment {}>".format(self.id)


class Visit(db.Model):
    __tablename__ = 'visit'

    visit_day = db.Column(db.CHAR, primary_key=True)
    visit_count = db.Column(db.Integer, nullable=False)

    def __init__(self, visit_day, visit_count):
        self.visit_day = visit_day
        self.visit_count = visit_count

    def __repr__(self):
        return "<Visit {}>".format(self.visit_day)
