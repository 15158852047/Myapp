from flask import render_template,session,request,flash,redirect,url_for,jsonify
from . import admin
from ..models import User
from functools import wraps
from sqlalchemy import or_
import json

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
def main(myid):
        c = 0
        u = User.query.offset((int(myid)-1)*10).limit(10).all()
        c = User.query.count()
        return render_template('admin/main.html',users=u,count=int(c/10+1),x=int(myid))


@admin.route('/upfor/<name>',methods=['GET','POST'])
def upfor(name):
    print (name)
    if int(name) == 0:
        flash('您还没有选择想要修改的会员！！')
        return redirect(url_for('admin.lookfor'))
    else:
        user = User.query.filter_by(username=name).first()
        return render_template('admin/upfor.html',user=user)




@admin.route('/lookfor/',methods=['GET','POST'])
def lookfor():
    return render_template('admin/lookfor.html')


@admin.route('/mohu/',methods=['GET','POST'])
def mohu():
    keyword = request.form.get('mydata')
    if keyword != '':
        users = User.query.filter(or_(User.username.like("%"+keyword+"%")),(User.name.like("%"+keyword+"%")),(User.password.like("%"+keyword+"%")),
                                 (User.tel.like("%" + keyword + "%"))).all()
        n = User.query.filter(or_(User.username.like("%" + keyword + "%")), (User.name.like("%" + keyword + "%")),
                                  (User.password.like("%" + keyword + "%")),
                                  (User.tel.like("%" + keyword + "%"))).count()
        x = []
        x.append(n)
        for user in users :
             x.append(user.to_json())
        print  (json.dumps(x))
        return json.dumps(x)
