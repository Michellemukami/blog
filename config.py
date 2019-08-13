import os

class Config:

   
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kami@localhost/blogger'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    QUOTES_API='http://quotes.stormconsultancy.co.uk/random.json'
class ProdConfig(Config):
     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kami@localhost/blogs_test'
   

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kami@localhost/blog'
    
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}