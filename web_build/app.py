#!/usr/bin/env python3
#! -*- coding:utf-8 -*-

import web
from flask import Flask
from flask import abort
from flask import  redirect
from flask import render_template

__author__ = 'Liguanh'


urls = (
    '/index', 'index',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello',
)

app = web.application(urls, globals())

app1 = Flask(__name__)

render = web.template.render('templates')

class blog:
    def POST(self):
        data = web.input()
        return data

    def GET(self):
        header = web.ctx.env
        return header

class index:
    def GET(self):
        query = web.input()
        return query


class hello:
    def GET(self, name):
        return render.form1(name = name)


if __name__ == '__main__':
    app.run()