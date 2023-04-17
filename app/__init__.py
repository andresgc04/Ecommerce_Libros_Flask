from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hola Mundo!, Código Facilito.'

def page_not_found(error):
    return render_template('errors/404.html'), 404

def inicializar_app(config):
    app.config.from_object(config)
    app.register_error_handler(404,page_not_found)
    return app
