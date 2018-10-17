from flask import render_template,session,request,flash,redirect,url_for,jsonify
from . import admin
from ..models import User,Product
from functools import wraps
from sqlalchemy import or_
from bson.objectid import ObjectId


@admin.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        u = User.objects(username=name,password=pwd).first()
        if u :
            if u.Role == 0:
                session['user_id'] = u.username
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
        u = User.objects((int(myid)-1)*10).limit(10).all()
        c = User.objects().count()
        return render_template('admin/main.html',users=u,count=int(c/10+1),x=int(myid))


@admin.route('/upfor/<name>',methods=['GET','POST'])
def upfor(name):
    print (name)
    if int(name) == 0:
        flash('您还没有选择想要修改的会员！！')
        return redirect(url_for('admin.lookfor'))
    else:
        user = User.objects(id=name).first()
        return render_template('admin/upfor.html',user=user)




@admin.route('/lookfor/',methods=['GET','POST'])
def lookfor():
    return render_template('admin/lookfor.html')


@admin.route('/mohu/',methods=['GET','POST'])
def mohu():
    keyword = request.form.get('mydata')
    print (keyword)
    if keyword != '':
        #users = User.objects(or_((User.username.like("%"+keyword+"%")),(User.name.like("%"+keyword+"%")))).all()
        users = User.objects({"$or":[{'name':{'$regex':keyword}},{'username':{'$regex':keyword}}]})
        print (users)
        x = []
        l = []
        for user in users :
            if user.name not in l :
                n = {'id':int(user.id),'uname':str(user.username),'pwd1':str(user.password),'na':str(user.name),'tel1':str(user.tel),'birth1':str(user.birth),'Role':int(user.Role)}
            #n = [user.username,user.password,user.name,user.tel,user.birth,user.Role]
                x.append(n)
                l.append(user.name)
       # print (x)
        return jsonify(x)


@admin.route('/lookorder/',methods=['GET','POST'])
def lookorder():
    return render_template('admin/lookorder.html')


@admin.route('/product/',methods=['GET','POST'])
def product():
    product = Product.objects().all()
    for i in product :
        f = open('app/static/admin/image/%s.png' % i.name,'wb')
        f.write(i.image.read())
        f.close()
    return render_template('admin/product.html',product=product)


@admin.route('/uppro/<name>',methods=['GET','POST'])
def uppro(name):
    pro = Product.objects(name=name).first()
    if request.method == 'POST':
        f = request.files['file']
        pro.delete()
        pr = Product(name=request.form.get('name'), money=request.form.get('money'),
                          Info=request.form.get('Info'), have=request.form.get('kucun'),
                          zhonglei=request.form.get('zhonglei'))
        pr.image.put(f)
        pr.save()
        return redirect(url_for('admin.product'))
    else:
        f = open('app/static/admin/image/%s.png' % pro.name, 'wb')
        f.write(pro.image.read())
        f.close()
        return render_template('admin/uppro.html',pro=pro)

@admin.route('/delpro/<name>',methods=['GET','POST'])
def delpro(name):
    pro = Product.objects(name=name).first()
    pro.delete()
    return redirect(url_for('admin.product'))



@admin.route('/addpro/',methods=['GET','POST'])
def addpro():
    if request.method == 'POST' :
        f = request.files['file']
        product = Product(name=request.form.get('name'),money=request.form.get('money'),
                          Info=request.form.get('Info'),have=request.form.get('kucun'),
                          zhonglei=request.form.get('zhonglei'))
        product.image.put(f)
        product.save()
        return redirect(url_for('admin.product'))
    return render_template('admin/addpro.html')


@admin.context_processor
def session_context():
    user_id = session.get('user_id')
    if user_id :
        user = User.objects(username=user_id).first()
        if user:
            return {'user':user}
    return {}