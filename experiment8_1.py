# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# #Content1:
# def log(func):
#    global i
#    def wraper(*args, **kw):
#        print("第{}个斐波那契数".format(i))
#        return func(*args, **kw)
#    return wraper

# i = 0
# x = 1
# y = 1
# @log
# def fibo():
#    global x
#    global y
#    x, y = y, x+y
#    return y
   
# if __name__ == '__main__':
#    for i in range(10):
#        print(fibo())


# #Content2:
# import functools

# def log(text):
#    def decorator(func):
#        @functools.wraps(func)
#        def wraper(*args, **kw):
#            print("%s %s():"%(text, func.__name__))
#            return func(*args, **kw)
#        return wraper
#    return decorator

# @log('excute')
# def now():
#    print("2018-12-11")

# if __name__ == '__main__':
#    now()
#    print(now.__name__)
    

# # Content3:
# from flask import Flask
# from flask import request
# from flask import make_response
# from flask import redirect
# app = Flask(__name__)

# @app.route('/')
# def index():
#    return '<h1>Hello World!</h1>'

# @app.route('/response')
# def respomse():
#    response = make_response('<h1>This document carries a cookie!</h1>')
#    response.set_cookie('answer', '42')
#    return response

# @app.route('/redirect')
# def redirect1():
#    return redirect('http://www.baidu.com')

# @app.route('/test')
# def test():
#    user_agent = request.headers.get('User-Agent')
#    return '<p>Your browser is %s</p>' % user_agent

# @app.route('/user/<name>')
# def user(name):
#    return '<h1>Hello, %s!</h1>' % name

# if __name__ == '__main__':
#    app.run(debug=True)



# #Content4:
# from flask import Flask, render_template
# from flask_bootstrap import Bootstrap
# app = Flask(__name__)
# bootstrap = Bootstrap(app)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name=name)

# if __name__ == '__main__':
#     app.run(debug=True)


#Content5:
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)



















