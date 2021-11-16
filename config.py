import os
class Config:

   UPLOADED_PHOTOS_DEST ='app/static/photos' 
   SECRET_KEY = '44zjgm_d2AM394JjigW7rQ'
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://access:1234567@localhost/blogg'  

#    email configurations
   MAIL_SERVER = 'smtp.googlemail.com'
   MAIL_PORT = 587
   MAIL_USE_TLS = True
   MAIL_USERNAME = 'juliana.alikutepa@student.moringaschool.com'
   MAIL_PASSWORD = 'Twinnie@123'


class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://access:1234567@localhost/blogg'
    DEBUG = True

class TestConfig(Config):'postgresql+psycopg2://access:1234567@localhost/blogg'
        


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}  