from flask import render_template,request,flash,redirect,url_for,session
from . import user
from ..models import User,Product,Order,BuyCar
from ..models import db

@user.route('/')
def index():
    products = Product.objects().limit(3)
    for i in products:
        f = open('app/static/image/%s.png' % i.name,'wb')
        f.write(i.image.read())
        f.close()
    return render_template('Main.html',products=products)

@user.route('/aboutyq')
def aboutyq():
    return render_template('aboutyq.html')

@user.route('/huojiang')
def huojiang():
    return render_template('huojiang.html')

@user.route('/qiyuan')
def qiyuan():
    return render_template('lishi.html')


@user.route('/aboutmx')
def aboutmx():
    return render_template('aboutmx.html')


@user.route('/login/',methods=['GET','POST'])
def login():
    if request.method  == 'POST':
        name = request.form.get('name')
        pass1 = request.form.get('pass')
        use = User.objects(username=name,password=pass1).first()
        if use:
            session['user_id'] = use.name
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
            use = User.objects(username=username).first()
            if use :
                flash('该用户已经存在！')
            else:
                tele = User.objects(tel=tel).first()
                if tele:
                    flash('改电话号码已经注册!')
                else:
                    add = User(username=username,password=pass1,tel=tel,birth=birth,name=name,money=0,jifen=0,Role=1)
                    add.save()
                    return redirect(url_for('user.login'))
    return render_template('regist.html')



@user.route('/addCar/')
def addCar():
    car = BuyCar(ProdName=request.form.get('name'),Price=request.form.get('money'),Num=request.form.get('count'),
                AllPrice=request.form.get('allmoney'),bname=session.get('user_id'))
    f = open('app/static/admin/image/%s.png' % request.form.get('name'), 'wb')
    car.image.put(f)
    car.save()
    return redirect(url_for('user.Car'))


@user.route('/Car/<name>')
def Car(name):
    cars =  BuyCar.objects(name=name).all()
    for car in cars :
        f = open('app/static/image/%s.png' % car.name,'wb')
        f.write(car.image.read())
        f.close()
    return render_template('car.html',cars=cars)



@user.route('/logout/')
def logout():
    session.pop('user_id')
    return redirect(url_for('Main.index'))


@user.route('/proinfo/<name>')
def proinfo(name):
    pro = Product.objects(name=name).first()
    return render_template('proinfo.html',pro=pro,name=session.get('user_id'))


@user.route('/addorder/',methods=['POST','GET'])
def addorder():
    s = request.form.get('name').strip()
    add = Order(ProdName=s,Price=request.form.get('money').strip(),Num=request.form.get('count').strip(),
                AllPrice=request.form.get('allmoney').strip(),isRead=0,oname=session.get('user_id'))
    f = open('app/static/admin/image/%s.png' % s, 'rb')
    add.image.put(f.read())
    f.close()
    add.save()
    return render_template('success.html')


@user.context_processor
def session_context():
    user_id = session.get('user_id')
    if user_id :
        user = User.objects(name=user_id).first()
        if user:
            return {'users':user}
    return {}
