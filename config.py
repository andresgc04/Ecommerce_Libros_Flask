from decouple import config

class Config:
    SECRET_KEY = 'B!1weNAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp-mail.outlook.com' 
    MAIL_PORT = 587 # TLS: Transport Layer Security (Seguridad De La Capa De Transporte).
    MAIL_USE_TLS = True
    MAIL_USER_NAME = 'andresgc1997@outlook.com'
    MAIL_PASSWORD = config('MAIL_PASSWORD')


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
