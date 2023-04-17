from app import inicializar_app
from config import config

configuration = config['development']

app = inicializar_app(configuration)

manager = app

if __name__ == '__main__':
    manager.run()