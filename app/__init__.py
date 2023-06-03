from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
import pymysql

from .models.ModelBook import ModelBook

app = Flask(__name__)

csrf = CSRFProtect()

# MySQL Connection:
def connection():
    server = 'localhost'
    user = 'root'
    password = ''
    db = 'storeDB'
    charset = 'utf8mb4'

    return pymysql.connect(host=server, user=user, password=password, database=db, charset=charset)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # CSRF (Cross-Site Request Forgery): Solicitud de falsificación entre sitios.

    if request.method == 'POST':
        if request.form['userName'] == 'admin' and request.form['password'] == '123456':
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/libros')
def list_books():
    try:
        books = ModelBook.list_books(connection(), pymysql)

        books_data = {'books' : books}

        return render_template('listado_libros.html', books_data = books_data)
    
    except Exception as ex:
        print(ex)


def page_not_found(error):
    return render_template('errors/404.html'), 404


def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, page_not_found)
    return app
