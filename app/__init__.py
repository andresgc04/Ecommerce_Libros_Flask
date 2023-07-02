from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import pymysql

from .models.ModelBuyBook import ModelBuyBook
from .models.ModelBook import ModelBook
from .models.ModelUser import ModelUser

from .models.entities.Purchasing import Purchasing
from .models.entities.Books import Books
from .models.entities.Users import Users

from .consts import *

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


login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(user_id):
    return ModelUser.get_user_by_id(connection(), pymysql, user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # CSRF (Cross-Site Request Forgery): Solicitud de falsificación entre sitios.
    if request.method == 'POST':

        user = Users(None, request.form['userName'],
                     request.form['password'], None)

        user_loged = ModelUser.login(connection(), user, pymysql)

        if user_loged != None:

            login_user(user_loged)

            flash(WELCOME_MESSAGE, 'success')

            return redirect(url_for('index'))
        else:
            flash(LOGIN_INVALID_CREDENTIALS, 'warning')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
def logout():
    logout_user()

    flash(LOGOUT, 'success')

    return redirect(url_for('login'))


@app.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        if current_user.user_type_id.user_type_id == 1:
            books_sold = []

            data = {
                'title': 'Libros Vendidos',
                'books_sold': books_sold
            }
        else:
            books_purchased = []

            data = {
                'title': 'Mis Compras',
                'books_purchased': books_purchased
            }

        return render_template('index.html', data=data)
    else:
        return redirect(url_for('login'))


@app.route('/libros')
@login_required
def list_books():
    try:
        books = ModelBook.list_books(connection(), pymysql)

        books_data = {
            'title': 'Listado De Libros',
            'books': books
        }

        return render_template('listado_libros.html', books_data=books_data)

    except Exception as ex:
        return render_template('errors/error.html', message=format(ex))


@app.route('/buyBook', methods=['POST'])
@login_required
def buy_book():
    data_request = request.get_json()

    data = {}

    try:
        book = Books(data_request['isbn'], None, None, None, None)

        book_purchase = Purchasing(None, book, current_user)

        data['success'] = ModelBuyBook.register_book_purchase(connection(), book_purchase, pymysql)
    except Exception as ex:
        data['message'] = format(ex)
        data['success'] = False
    return jsonify(data)


def unauthorized_site(error):
    return redirect(url_for('login'))


def page_not_found(error):
    return render_template('errors/404.html'), 404


def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(401, unauthorized_site)
    app.register_error_handler(404, page_not_found)
    return app
