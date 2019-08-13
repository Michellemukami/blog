import os

class Config:

   
    SECRET_KEY = 'kamikaze'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kami@localhost/blogger'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    MAIL_USERNAME = "michellemukami.g@gmail.com"
    MAIL_PASSWORD = "kamikaze@99"
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    QUOTES_API='http://quotes.stormconsultancy.co.uk/random.json'
class ProdConfig(Config):
     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kami@localhost/blogger'
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kami@localhost/blogger_test'
   

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michelle:kami@localhost/blogger'
    
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}