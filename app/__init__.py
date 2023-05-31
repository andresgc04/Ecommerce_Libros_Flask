from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        if request.form['userName'] == 'admin' and request.form['password'] == '123456':
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


def page_not_found(error):
    return render_template('errors/404.html'), 404

def inicializar_app(config):
    app.config.from_object(config)
    app.register_error_handler(404,page_not_found)
    return app
