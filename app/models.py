from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager

 
class PhotoProfile(db.Model):

   __tablename__ = 'profile_photos'

   id = db.Column(db.Integer,primary_key = True)
   pic_path = db.Column(db.String())
   user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

class Category(db.Model):
    __tablename__="categories"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))


class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.Integer, primary_key = True )
    title = db.Column(db.String(100))
    content = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    
    
    
    def __repr__(self):
        return f"Blog('{self.title}')"

    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def clear_blog(cls):
        blogs.all_blogs.clear()



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    blog = db.relationship('Blog', backref = 'users', lazy="dynamic")
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    password = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    
   
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    
   

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    


class Comment(db.Model):
    comment = db.Column(db.String(100))
    pitch_id = db.Column(db.Integer, db.ForeignKey('blog.id'))
    comment_id = db.Column(db.Integer, primary_key = True)
    def __repr__(self):
        return f"Comment('{self.comment}')"

class Quote:
    def __init__(self,quote,author):
        self.quote=quote
        self.author=author

    