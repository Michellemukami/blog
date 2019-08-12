from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import BlogForm,CommentForm
from app.request import get_quote
from ..models import Blog,User,Comment
from flask_login import login_required, current_user
from .forms import UpdateProfile
from .. import db,photos
import markdown2 
@main.route("/pitches")
def posts():
    form = CommentForm()
    post = Pitch.query.get_or_404()
    comments = Comment.query.all()

    if form.validate_on_submit():
        comment = Comment(comment=form.comment.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('posts.post'))
    return render_template('post.html', title = post.title, posts = posts,comments=comments, form=form)

@main.route("/post/new", methods= ['GET', 'POST'])
@login_required
def new_post():

    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(title=form.title.data, content = form.content.data, category = form.category.data)
        db.session.add(blog)
        db.session.commit()
        
        return redirect(url_for('main.home'))
    return render_template('post.html',title = 'New Post', form = form, legend = 'New Post')

@main.route("/")
@main.route("/home")
def home():

   '''
   View root page function that returns the index page and its data
   '''
   title = 'Welcome to Pitch app'

    
   page = request.args.get('page', 1, type=int)
   posts=Blog.query.all()
   quotes = get_quote()
   
   return render_template('home.html',posts=posts,quotes=quotes)

@main.route('/pitches/inspiration')
def inspiration():
    posts=Blog.query.filter_by(category='Inspirational')

    return render_template('inspirational.html', posts=posts)


@main.route('/pitches/biography')
def biograpghy():
    posts=Blog.query.filter_by(category='Biography')

    return render_template("biograghy.html", posts=posts)
@main.route('/user/<uname>/post')
def user_post(uname):
   
   user = User.query.filter_by(username=uname).first()
   blog = Blog.query.filter_by(users=user).all()
 

   return render_template("profile/user_posts.html", users=user,posts=posts,blog=blog)

@main.route('/pitches/idea')
def idea():

   posts=Blog.query.filter_by(category='Ideas')

   return render_template("ideas.html", posts=posts)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
@main.route('/comment')
def comment():
    form = CommentForm()
    posts = Blog.query.all()
    comment = Comment.query.all()

    if form.validate_on_submit():
        comment = Comment(comment=form.comment.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.comment',))
    return render_template('new_comment.html', posts = posts,comment=comment, comment_form=form)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route("/post/update", methods= ['GET', 'POST'])
@login_required
def update_post():
    posts = Blog.query.all
   
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(title=form.title.data, content = form.content.data, category = form.category.data)

        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('main.home'))
    elif request.method == 'GET':

        blog = Blog(title=form.title.data, content = form.content.data, category = form.category.data)
    return render_template('post.html',title = 'Update Post', Blog_form = form, legend = 'Update Post',posts=posts)


@main.route("/post/delete", methods= ['GET','POST'])
@login_required
def delete_post():
    posts = Blog.query.all()
    if post.author != current_user:
        abort(403)
    db.session.delete(posts)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
    