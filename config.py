DEBUG = True



HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'Myapp'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,
                                                              HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI