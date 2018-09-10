from flask import render_template,request,flash,redirect,url_for,session
from . import user
from ..models import User
from ..models import db

@user.route('/')
def index():
    return render_template('Main.html')

@user.route('/login/',methods=['GET','POST'])
def login():
    if request.method  == 'POST':
        name = request.form.get('name')
        pass1 = request.form.get('pass')
        use = User.query.filter_by(username=name,password=pass1).first()
        if use:
            session['user_id'] = use.id
            session.permanet = True
            return  redirect(url_for('user.index'))
        else:
            flash('账号或密码错误!!')
            return render_template('login.html')
    else:
        return render_template('login.html')


@user.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'POST':
        username = request.form.get('username')
        pass1 = request.form.get('password1')
        pass2 = request.form.get('password2')
        name = request.form.get('name')
        tel = request.form.get('tele')
        birth = request.form.get('birth')
        if pass1 != pass2 :
            flash('两次密码不一致，请重新填写')
        else:
            use = User.query.filter_by(username=username).first()
            if use :
                flash('该用户已经存在！')
            else:
                tele = User.query.filter_by(tel=tel).first()
                if tele:
                    flash('改电话号码已经注册!')
                else:
                    add = User(username=username,password=pass1,tel=tel,birth=birth,name=name,money=0,jifen=0)
                    db.session.add(add)
                    db.session.commit()
                    return redirect(url_for('user.login'))
    return render_template('regist.html')



@user.route('/logout/')
def logout():
    session.pop('user_id')
    return redirect(url_for('Main.index'))



@user.context_processor
def session_context():
    user_id = session.get('user_id')
    if user_id :
        user = User.query.filter_by(id=user_id).first()
        if user:
            return {'user':user}
    return {}
