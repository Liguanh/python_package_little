#!/usr/bin/env python3
#! -*- coding:utf-8 -*-

__author__ = 'Liguanh'

from flask import Flask, url_for
from flask import abort
from flask import render_template
from flask import redirect
from flask import request

app = Flask(__name__)


@app.route('/index')
def index():
    #return redirect('http://www.baidu.com')
    attribute = {
        'username': 'linguanghui',
        'message': 'Bad Request'
    }
    return render_template('form.html', attribute = attribute)


@app.route('/blog/123', methods=['POST'])
def blog():
    if not request.form['password']:
        return redirect(url_for('index'))

    return request.form['username']

@app.route('/hears', methods=['GET'])
def hears():
    return 'hah'

if __name__ == '__main__':
    app.run(debug=True)