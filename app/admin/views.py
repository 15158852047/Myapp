from flask import render_template,session,request,flash,redirect,url_for
from . import admin
from ..models import User
from functools import wraps

@admin.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        u = User.query.filter_by(username=name,password=pwd).first()
        if u :
            if u.Role == 0:
                session['user_id'] = u.id
                session.permanet = True
                return redirect(url_for('admin.main',myid=1))
            else:
                flash('您并不是管理员，无法进入后台!')
                return render_template('admin/login.html')
        else:
            flash('用户不存在!')
            return render_template('admin/login.html')

    return render_template('admin/login.html')


def login_required(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if session.get('user_id'):
                return func(*args, **kwargs)
            else:
                return redirect(url_for('admin.index'))
            return func(*args, **kwargs)

        return wrapper



@admin.route('/main/<myid>',methods=['GET','POST'])
#@login_required
def main(myid=1):
        c = 0
        u = User.query.offset((int(myid)-1)*10).limit(10).all()
        c = User.query.count()
        print (c/10+1)
        print (myid)
        return render_template('admin/main.html',users=u,count=int(c/10+1),x=int(myid))




